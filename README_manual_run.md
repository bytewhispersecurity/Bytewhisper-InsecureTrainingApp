## Running manually without docker 

### Prerequisites
To build locally
* [Node.js](https://nodejs.org/en) and npm installed
* [Svelte](https://svelte.dev/)
* [Ollama](https://ollama.com/) and any GPT model
* [Python](https://python.org/)

## Installation
1. Clone the repository:
```shell
git clone https://github.com/bytewhispersecurity/Bytewhisper-InsecureApp.git
cd Bytewhisper-InscureApp
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
While inside the `Bytewhisper-InsecureApp` directory you will need to run the web server.
2. Start the development server:
```shell
cd frontend
npm run dev
```
You will need to open up another terminal in the `Bytewhisper-InsecureApp` directory to run the flask app to route our queries through the secruity controls.
3. Start the flask app for llm-guard:
```shell
cd backend
python3 app.py
```