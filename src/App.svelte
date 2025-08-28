<script>
    import { onMount } from 'svelte';
    import { Router, Route } from 'svelte-routing';
    import InsecureAppHeader from './libs/components/Header.svelte';
    import InsecureAppFooter from './libs/components/Footer.svelte';
    import Logs from './routes/Logs.svelte';

    let query = '';
    let response = '';
    let isLoading = false;
    

    function updateFavicon() {
        const lightFavicon = document.getElementById('light-favicon');
        const darkFavicon = document.getElementById('dark-favicon');
        if (lightFavicon && darkFavicon) {
            if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                lightFavicon.removeAttribute('rel');
                darkFavicon.setAttribute('rel', 'icon');
            } else {
                darkFavicon.removeAttribute('rel');
                lightFavicon.setAttribute('rel', 'icon');
            }
        }
    }

    async function sendRequest() {
        if (!query.trim()) return;
        const userMessage = { role: 'user', content: query };
        isLoading = true;

        try {
            const res = await fetch('http://localhost:5001/chat', {
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

    onMount(() => {
        // Update favicon on initial load
        updateFavicon();
        // Update favicon on color scheme change
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        mediaQuery.addEventListener('change', updateFavicon);

        // Cleanup listener on component destroy
        return () => {
            mediaQuery.removeEventListener('change', updateFavicon);
        };
    });
</script>
<div class="main-background min-h-screen justify-between al-center">
    <InsecureAppHeader />
    <Router>
        <Route path="/">
            <main>
                <h1>Query your local AI</h1>
                <div>
                    <input class="input-box" type="text" bind:value={query} placeholder="Enter your query" maxlength="200" on:keydown={(e) => e.key === 'Enter' && sendRequest()} />
                    <button on:click={sendRequest} disabled={isLoading}>
                        {isLoading ? 'Loading...' : 'Submit'}
                    </button>
                </div>
                <div>
                    <p>{response || 'No response yet.'}</p>
                </div>
            </main>
        </Route>
        <Route path="/logs">
            <Logs />
        </Route>
    </Router>
    <InsecureAppFooter />
</div>