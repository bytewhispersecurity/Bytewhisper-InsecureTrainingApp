import json
import requests
import argparse

url = "http://localhost:5001/scan"
headers = {"Content-Type": "application/json"}

offensive_prompts = {
    "direct": {
        "1": "direct prompt injection 1",
        "2": "direct prompt injection 2",
        "3": "direct prompt injection 3"
    },
    "indirect": {
        "1": "indirect prompt injection 1",
        "2": "indirect prompt injection 2",
        "3": "indirect prompt injection 3"
    },
    "contextual": {
        "1": "contextual prompt injection 1",
        "2": "contextual prompt injection 2",
        "3": "contextual prompt injection 3"
    },
    "role-playing": {
        "1": "role-playing prompt injection 1",
        "2": "role-playing prompt injection 2",
        "3": "role-playing prompt injection 3"
    },
    "technical": {
        "1": "technical prompt injection 1",
        "2": "technical prompt injection 2",
        "3": "technical prompt injection 3"
    }
}

# TODO - Add iterations to the prompt sending function
def send_prompt(prompt) -> list:
    payload = {
        "query": prompt
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    result = []
    if response.status_code == 200:
        result.append(response.json())
    else:
        result.append(f"Error: {response.status_code}")
    return result
    
def generate_prompts(file_path: str = "prompts.json", tier: int = 1, attack: str = "direct") -> str:
    id = offensive_prompts[attack][str(tier)]
    with open(file_path, 'r') as file:
        prompts = json.load(file)
        for prompt in prompts:
            if prompt['id'] == id:
                return prompt['prompt']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM Attack Simulation", epilog="This tool is meant to test site defenses and should be used responsibly.")
    parser.add_argument('-p', '--prompt', type=str, help="Custom prompt to send to the LLM")
    parser.add_argument('-t', '--tier', type=int, choices=[1, 2, 3], help="Tier of the attack (1: Basic, 2: Intermediate, 3: Advanced)")
    parser.add_argument('-a', '--attack', type=str, help="Type of prompt attack to simulate (options: direct, indirect, contextual, role-playing, technical)")
    # parser.add_argument('-i', '--iterations', type=int, default=1, help="Number of iterations to run the attack prompt")
    parser.add_argument('-f', '--file', type=str, help="File containing prompts to send to the LLM")
    parser.add_argument('-o', '--output', type=str, help="File to save the results")
    args = parser.parse_args()
    
    tier = 1 if args.tier is None else str(args.tier)
    attack = 'direct' if args.attack is None else args.attack
    file_path = 'prompts.json' if args.file is None else args.file
    # iterations = 1 if args.iterations is None else args.iterations
    output_file = 'results.json' if args.output is None else args.output
    
    if args.prompt:
        prompt = args.prompt
    else:
        prompt = generate_prompts(file_path, tier, attack)

    result = send_prompt(prompt, iterations)
    print(result)