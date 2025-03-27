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

Run with Docker
* [Docker](https://www.docker.com/)

## Installation
1. Clone the repository:
```shell
git clone https://github.com/<place-holder>/<place-holder>.git
cd <place-holder>
```
2. Install dependencies:
```shell
npm install
```
## Running the Application
1. Start Ollama:
```shell
ollama run <model-name>
```
2. Star the development server:
```shell
npm run dev
```
## Usage
### Prompt Injection
A text box wil present to test out prompts. You will be able to build remediations and test your efforts.