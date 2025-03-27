<script>
    import { onMount } from 'svelte';
    import { Ollama } from 'ollama';
    let query = '';
    let response = '';
    let isLoading = false;
    let selectedFile = null;

    // This function sends user request to the LLM
    async function fetchResponse() {
        if (!query.trim()) return;

        isLoading = true;
        response = '';

        try {
            const prompt = createPrompt(query) || '';
            const ollama = new Ollama();
            const res = await ollama.chat({
                model: 'llama3.1',
                messages: [{role:'user', content: prompt}]
            });
            response = res.message.content;
        } catch (error) {
            response = error.message;
        } finally {
            isLoading = false;
        }
    }

    // This function sends file content to the LLM
    async function handleFileUpload() {
        if (!selectedFile) return;

        isLoading = true;
        response = '';

        try {
            const reader = new FileReader();
            reader.onload = async (e) => {
                const fileContent = e.target.result;
                const ollama = new Ollama();
                const res = await ollama.chat({
                    model: 'llama3.1',
                    messages: [{
                        role: 'user',
                        content: `Analyze this file content: ${fileContent}`
                    }]
                });
                response = res.message.content;
                isLoading = false;
            };
            reader.readAsText(selectedFile);
        } catch (error) {
            response = error.message;
            isLoading = false;
        }
    }

    // This function will validatte user input
    function validateInput(input) {
        const validPattern = /[^a-zA-Z0-9]+/; // Adjust these based on your requirements
        return validPattern.test(input); 
    }
    // This function will sanitize user input
    function sanitizeInput(input) {
        return input.replace(/[^a-zA-Z0-9]+/, ''); // Remove special characters
    }

    // This function will create a valid prompt for the LLM
    function createPrompt(userInput) {
        const systemPrompt = "Prompt: Please follow the instructions below to get the best results. \n";
        if (validateInput(userInput)) {
            const userPrompt = `User: ${sanitizeInput(userInput)}`;
            return `${systemPrompt}\n${userPrompt}`;
        } else {
            console.log("Invalid input. Please enter a valid input.");
        }
    }
</script>

<main>
    <h1>Query your local LLM</h1>
    <div>
        <div class="file-upload">
            <input
                type="file"
                id="file"
                accept=".txt"
                placeholder="Upload a file"
                on:change={(e) => {
                    const file = e.target.files[0];
                    if (file && file.type === 'text/plain') {
                        selectedFile = file;
                    } else {
                        selectedFile = null;
                        alert('Please upload a valid text file.');
                    }
                }}
            />
            <button on:click={handleFileUpload} disabled={!selectedFile || isLoading}>
                {isLoading ? 'Uploading...' : 'Upload File'}
            </button>
        </div>
        <input
            type="text"
            bind:value={query}
            placeholder="Enter your query"
            on:keydown={(e) => e.key === 'Enter' && fetchResponse()}
        />
        <button on:click={fetchResponse} disabled={isLoading}>
            {isLoading ? 'Loading...' : 'Submit'}
        </button>
    </div>
    <div>
        <h2>Response:</h2>
        <div style="max-width: 600px; max-height: 300px; overflow-y: auto; border: 1px; padding: 10px; margin-top: 10px;">
            <p>{response || 'No response yet.'}</p>
        </div>
    </div>
</main>