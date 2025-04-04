# Insecure LLM Application
Welcome to ByteWhisper's LLM focused Vulnerability Remediation Project. This project aims to educate users on how to identify and remediate known vulnerabilities in Large Language Models (LLMs) using Ollama local models. By integrating these models into a Svelte application, we provide practical examples and solutions. 

## Vulnerabilities Implemented
* [Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

## Getting Started
### Prerequisites
To build locally
* [Node.js](https://nodejs.org/en) and npm installed
* [Svelte](https://svelte.dev/)
* [Ollama](https://ollama.com/) and any GPT model
* [Python](https://python.org/)

## Installation
1. Clone the repository:
```shell
git clone https://github.com/bytewhispersecurity/ByteWhisper-InsecureApp.git
cd ByteWhisper-InscureApp
```
2. Install dependencies:
```shell
npm install
pip install -r requirements.txt
```
## Running the Application
Ensure that you have Ollama running, and pull down the model you wish to use. In our testing we used llama 3.1.
1. Start Ollama:
```shell
ollama pull llama3.1
```
While inside the `ByteWhisper-InsecureApp` directory you will need to run the web server.
2. Start the development server:
```shell
npm run dev
```
You will need to open up another terminal in the `ByteWhisper-InsecureApp` directory to run the flask app to route our queries through the secruity controls.
3. Start the flask app for llm-guard:
```shell
python llm-guard.py
```

## Usage
In your web browser navigate to `http://localhost:5173` once you have started the three services needed.
### Prompt Injection
A text box wil present to test out prompts. You will be able to build remediations and test your efforts.