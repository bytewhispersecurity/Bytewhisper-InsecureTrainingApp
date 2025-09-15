<script lang="ts">
    import { onMount } from "svelte";
    import {
        Table,
        TableHead,
        TableHeadCell,
        TableBody,
        TableBodyRow,
        TableBodyCell,
        Textarea,
    } from "flowbite-svelte";

    type LogEntry = {
        timestamp: string;
        user_prompt: string;
        system_prompt: string;
        output_message: string;
        risk_score: number;
    };

    let logs: LogEntry[] = [];

    onMount(async () => {
        try {
            const response = await fetch("http://localhost:5001/logs", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            logs = await response.json();
        } catch (error) {
            console.error("Failed to fetch logs:", error);
        }
    });
</script>

<main>
    <div class="flex-container">
        <div class="row table-class">
            <h1>Daily logs</h1>
            {#if logs.length === 0}
                <p>No logs available.</p>
            {:else}
                <Table striped={true} shadow={true} hoverable={true} color="default" class="table-class">
                    <TableHead class="table_header">
                        <TableHeadCell>Logs</TableHeadCell>
                    </TableHead>
                    <TableBody>
                        {#each logs as log}
                            <TableBodyRow>
                                <TableBodyCell class="blacktext">
                                    <table class="w-full">
                                    <tbody>
                                        <tr><td>
                                        <strong>{new Date(
                                            log.timestamp,
                                        ).toLocaleString()}</strong
                                    ></td></tr>
                                    <tr><td>
                                        <strong>User Input:</strong><br>
                                        <Textarea
                                            disabled="disabled"
                                            id="textarea-id"
                                            placeholder="Null"
                                            rows={4}
                                            name="message"
                                            bind:value={log.user_prompt}
                                            class="w-full blacktext"
                                        />
                                    </td></tr>
                                    <tr><td>
                                        <strong>Prompt:</strong><br>
                                        <Textarea
                                            disabled="disabled"
                                            id="textarea-id"
                                            placeholder="Null"
                                            rows={4}
                                            name="message"
                                            bind:value={log.system_prompt}
                                            class="w-full blacktext"
                                        />
                                    </td></tr>
                                    <tr><td>
                                        <strong>Response:</strong><br>
                                        <Textarea
                                            disabled="disabled"
                                            id="textarea-id"
                                            placeholder="Null"
                                            rows={4}
                                            name="message"
                                            bind:value={log.output_message}
                                            class="w-full blacktext"
                                        />
                                    </td></tr>
                                    <tr><td>
                                        <strong>Risk Score:</strong>
                                        {log.risk_score}
                                    </td></tr>
                                    </tbody>
                                    </table>
                                </TableBodyCell>
                            </TableBodyRow>
                        {/each}
                    </TableBody>
                </Table>
            {/if}
        </div>
    </div>
</main>
