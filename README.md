# ⚠️ Warning ⚠️
This app is **insecure** on purpose. Do not expose it to the internet!

# ⚠️ **Insecure LLM Application** ⚠️

# Bytewhisper LLM Security Training App
Welcome to Bytewhisper's LLM focused Vulnerability Remediation Project. This project aims to educate users on how to identify and remediate known vulnerabilities in Large Language Models (LLMs) using Ollama local models. By integrating these models into a Svelte application, we provide practical examples and solutions.

## Vulnerabilities Implemented
* [Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

## Security Training Features
 
### Difficulty Levels
1. **Level 1 - Basic**: Simple prompt injection scenarios
2. **Level 2 - Intermediate**: More complex scenarios
3. **Level 3 - Advanced**: Sophisticated protection mechanisms to bypass

> Higher levels have the same target but 'harder' and more restrictive prompts.

## Getting Started

### Prerequisites
* [docker](https://www.docker.com/)
* [Ollama](https://ollama.com/) and any GPT model

### Running the Application
Ensure that you have Docker and Ollama running.
Pull down the model you wish to use.
In our testing we used llama 3.1.

##### Start Ollama:
```shell
$ ollama serve
```
##### In a separate shell pull a model
```shell
$ ollama pull llama3.1
```

While inside the `Bytewhisper-InsecureTrainingApp` directory you will need to run the docker compose file.
##### Start Docker App:
```shell
$ docker compose up --build
```

## Usage

Now that the application is running, open your web browser and go to the this URL: [http://localhost:3000](http://localhost:3000). A text box will be available to test out prompts. You will be able to build remediations and test your efforts. Try to ask your local model some simple questions such as: 
* "How many apples are consumed in the USA during a calendar year?" which will give you some interesting information. 
* "Are you running locally?" and you will see the limitations of the model as it is 100% positive it is not.

## 📚 Additional Resources
- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

## 📝 License
This project is licensed under the MIT License with additional security disclaimers - see the [LICENSE](LICENSE) file for details.