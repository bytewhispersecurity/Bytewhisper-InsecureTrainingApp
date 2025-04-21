import re
import ollama
import unicodedata

from llm_guard.input_scanners import PromptInjection
from llm_guard.output_scanners import Sensitive
from llm_guard.input_scanners.prompt_injection import MatchType

# Validate user input based on unicode categories
def validateInput(prompt: str) -> bool:
    # Create a tuple of allowed categories for Unicode characters
    allowed_categories = ('Lu', 'Ll', 'Zs', 'Nd', 'Po')
    # Check if the prompt contains allowed characters and spaces
    for char in prompt:
        cat = unicodedata.category(char)
        if cat in allowed_categories:
            continue
        return False
    return True

# Sanitize user input to remove unwanted characters, and optionally replace them with a special character
def sanitizeInput(prompt: str):
    return re.sub(r'[^a-zA-Z0-9]+/gm', '', prompt)

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
