<script>
    import { onMount } from 'svelte';
    import { Ollama } from 'ollama';
    let query = '';
    let response = '';
    let isLoading = false;

    // This function will send user query to the listening flask app
    async function sendRequest() {
        if (!query.trim()) return;
        isLoading = true;
        
        try {
            const res = await fetch('http://0.0.0.0:5001/scan', {
                method: 'POST',
                mode: 'cors',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ query })
            });
            const result = await res.json();
            response = result.response;
        } catch (error) {
            console.error('Error:', error);
            response = 'Error occurred while fetching response.';
        } finally {
            isLoading = false;
        }
    }
</script>

<main>
    <h1>Query your local LLM</h1>
    <div>
        <input
            type="text"
            bind:value={query}
            placeholder="Enter your query"
            maxlength="200"
            on:keydown={(e) => e.key === 'Enter' && sendRequest()}
        />
        <button on:click={sendRequest} disabled={isLoading}>
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