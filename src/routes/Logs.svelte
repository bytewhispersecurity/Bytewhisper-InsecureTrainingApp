<script lang="ts">
    import { onMount } from 'svelte';

    type LogEntry = {
        timestamp: string;
        user_input: string;
        prompt: string;
        response: string;
        risk_score: number;
    };

    let logs: LogEntry[] = [];

    onMount(async () => {
        try {
            const response = await fetch('http://0.0.0.0:5001/logs', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            logs = await response.json();
        } catch (error) {
            console.error('Failed to fetch logs:', error);
        }
    });
</script>

<main>
    <h1>Daily logs</h1>
    {#if logs.length === 0}
        <p>No logs available.</p>
    {:else}
        <ul>
            {#each logs as log }
                <li>
                    <strong>{new Date(log.timestamp).toLocaleString()}</strong>
                    <p><strong>User Input:</strong> {log.user_input}</p>
                    <p><strong>Prompt:</strong> {log.prompt}</p>
                    <p><strong>Response:</strong> {log.response}</p>
                    <p><strong>Risk Score:</strong> {log.risk_score}</p>
                </li>
            {/each}
        </ul>
    {/if}
</main>