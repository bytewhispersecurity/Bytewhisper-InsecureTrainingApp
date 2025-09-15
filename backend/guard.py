import re
import ollama
# import unicodedata

from llm_guard.input_scanners import PromptInjection
from llm_guard.output_scanners import Sensitive
from llm_guard.input_scanners.prompt_injection import MatchType

# Raw delimiter patterns (without safe-escape support)
delimiter = [
    r"\-\-\- Begin User Input: \-\-\-",
    r"\-\-\- End User Input: \-\-\-",
    r"\#\#\# Begin System Prompt: \#\#\#",
    r"\#\#\# End System Prompt: \#\#\#",
]

# Escape-aware regex (allows -%-%-% Begin User Input: %-%-%- and -%-%-% End User Input: %-%-%-, and #%#%#% Begin System Prompt: %%%#%#%# and #%#%#% End System Prompt: %%%#%#%#)
delimiter_escaped = [
    r"\-\%?\-\%?\-\%? Begin User Input: \%?\-\%?\-\%?\-",
    r"\-\%?\-\%?\-\%? End User Input: \%?\-\%?\-\%?\-",
    r"\#\%?\#\%?\#\%? Begin System Prompt: \%?\#\%?\#\%?\#",
    r"\#\%?\#\%?\#\%? End System Prompt: \%?\#\%?\#\%?\#",
]

# Strict patterns that do *not* allow for any escape sequences
delimiter_strict = [
    r"(?<!%)\-\-\- Begin User Input: \-\-\-(?!%)",
    r"(?<!%)\-\-\- End User Input: \-\-\-(?!%)",
    r"(?<!%)\#\#\# Begin System Prompt: \#\#\#(?!%)",
    r"(?<!%)\#\#\# End System Prompt: \#\#\#(?!%)",
]

def validateInput(prompt: str) -> bool:
    """Validate input for chat by checking for delimiters"""
    # Create a regex pattern that matches any of the delimiters
    pattern = re.compile("|".join(delimiter_strict), re.DOTALL)
    return not bool(pattern.search(prompt))

def sanitizeInput(prompt: str) -> str:
    """Sanitize the input for chat by removing any delimiters to prevent escaps of context."""
    # Create a regex pattern that matches any of the delimiters
    pattern = re.compile("|".join(delimiter_strict), re.DOTALL)
    # Remove the delimiters from the input
    sanitized_prompt = re.sub(pattern, "", prompt)
    return sanitized_prompt

def normalizeInput(prompt: str) -> str:
    """
    Convert safe-escaped delimiters to usable format.
    for example, -%-%-% Begin User Input: %-%-%- becomes --- Begin User Input: ---
    """
    escape_clean_delimiter = re.compile(r"(\-\%?\-\%?\-\%? Begin User Input: \%?\-\%?\-\%?\-)|"
                                       r"(\-\%?\-\%?\-\%? End User Input: \%?\-\%?\-\%?\-)|"
                                       r"(\#\%?\#\%?\#\%? Begin System Prompt: \%?\#\%?\#\%?\#)|"
                                       r"(\#\%?\#\%?\#\%? End System Prompt: \%?\#\%?\#\%?\#)")
    # Replace the safe-escaped delimiters with the actual delimiters
    return re.sub(escape_clean_delimiter, replacer, prompt)

def replacer(match):
    """
    Convert safe-escaped limiters back to usable format.
    for example, -%-%-% Begin User Input: %-%-%- becomes --- Begin User Input: ---
    """
    if match.group(1) is not None:
        return f"[{match.group(1)}]"
    elif match.group(2) is not None:
        return f"[{match.group(2)}]"
    elif match.group(3) is not None:
        return f"[{match.group(3)}]"
    return match.group(0) # Return the original match if no groups are found

# Send the sanitized input to the Ollama model
def get_ollama_response(user_input: str, system_input: str):
    if validateInput(user_input):
        sanitized_prompt = sanitizeInput(user_input)
        # encoded_prompt = encodeInput(sanitized_prompt)
        user_prompt = {
           "role": "user",
            "content": "--- Begin User Input: ---\n" + sanitized_prompt + "\n--- End User Input ---\n"
        }
        response = ollama.chat(model='llama3.1', messages=[system_input, user_prompt])
        return response['message']['content']
    else:
        return "Invalid input. Please use only alphanumeric characters."

def input_scanner(prompt: str):
    input_scanner = PromptInjection(threshold=0.5, match_type=MatchType.FULL)
    user_prompt, is_valid, risk_score = input_scanner.scan(prompt)
    if risk_score < 0.5:
        return user_prompt, risk_score
    else:
        return "Dangerous input detected. Please rephrase your question.", risk_score

def output_scanner(prompt: str, response: str):
    output_scanner = Sensitive(entity_types=["PERSON", "EMAIL"], redact=True)
    sanitized_output, is_valid, risk_score = output_scanner.scan(prompt, response)
    if risk_score < 0.5:
        return sanitized_output, risk_score
    else:
        return "Sensitive data detected. Please rephrase your question.", risk_score
