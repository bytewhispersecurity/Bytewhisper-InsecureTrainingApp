<script lang="ts">
    import { onMount } from "svelte";
    import {
        Select,
        Label,
        Table,
        TableHead,
        TableHeadCell,
        TableBody,
        TableBodyRow,
        TableBodyCell,
        Textarea,
    } from "flowbite-svelte";
    import { Router, Route } from "svelte-routing";
    import InsecureAppHeader from "./libs/components/Header.svelte";
    import InsecureAppFooter from "./libs/components/Footer.svelte";
    import Logs from "./routes/Logs.svelte";

    let query = $state("");
    let response = $state("");
    let isLoading = $state(false);
    let level = $state("1");

    let levels = [
        { value: "1", name: "Level 1" },
        { value: "2", name: "Level 2" },
        { value: "3", name: "Level 3" },
        { value: "4", name: "Level 4" },
        { value: "5", name: "Level 5" },
        { value: "6", name: "Level 6" },
        { value: "7", name: "Level 7" },
        { value: "8", name: "Level 8" },
    ];

    function updateFavicon() {
        const lightFavicon = document.getElementById("light-favicon");
        const darkFavicon = document.getElementById("dark-favicon");
        if (lightFavicon && darkFavicon) {
            if (
                window.matchMedia &&
                window.matchMedia("(prefers-color-scheme: dark)").matches
            ) {
                lightFavicon.removeAttribute("rel");
                darkFavicon.setAttribute("rel", "icon");
            } else {
                darkFavicon.removeAttribute("rel");
                lightFavicon.setAttribute("rel", "icon");
            }
        }
    }

    async function sendRequest() {
        if (!query.trim()) return;
        const userMessage = { role: "user", content: query };
        isLoading = true;

        try {
            const res = await fetch("http://localhost:5001/chat", {
                method: "POST",
                mode: "cors",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ query, level }),
            });
            const result = await res.json();
            response = result.response;
        } catch (error) {
            console.error("Error:", error);
            response = "Error occurred while fetching response.";
        } finally {
            isLoading = false;
        }
    }

    onMount(() => {
        // Update favicon on initial load
        updateFavicon();
        // Update favicon on color scheme change
        const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
        mediaQuery.addEventListener("change", updateFavicon);

        // Cleanup listener on component destroy
        return () => {
            mediaQuery.removeEventListener("change", updateFavicon);
        };
    });
</script>

<div class="main-background min-h-screen justify-between al-center">
    <InsecureAppHeader />
    <Router>
        <Route path="/">
            <main>
                <div class="flex-container">
                    <div class="row">
                        <h1>Query your local AI</h1>
                        <div>
                            <Table
                                striped
                                shadow
                                hoverable={true}
                                class="table-class"
                            >
                                <TableHead class="table_header table-class">
                                    <TableHeadCell>Chat</TableHeadCell>
                                </TableHead>
                                <TableBody>
                                    <TableBodyRow>
                                        <TableBodyCell>
                                            <Label>
                                                <span>Query entry</span><br />
                                                <input
                                                    class="input-box"
                                                    type="text"
                                                    bind:value={query}
                                                    placeholder="Enter your query"
                                                    maxlength="200"
                                                    onkeydown={(e) =>
                                                        e.key === "Enter" &&
                                                        sendRequest()}
                                                /><br />
                                            </Label><br />
                                            <Label>
                                                <span>Level select</span><br />
                                                <Select
                                                    class="input-box"
                                                    items={levels}
                                                    bind:value={level}
                                                /><br />
                                            </Label>
                                            <button
                                                class="whitetext"
                                                onclick={sendRequest}
                                                disabled={isLoading}
                                            >
                                                {isLoading
                                                    ? "Loading..."
                                                    : "Submit"}
                                            </button>
                                        </TableBodyCell>
                                    </TableBodyRow>
                                </TableBody>
                            </Table>

                            <p></p>
                            <Table
                                striped
                                shadow
                                hoverable={true}
                                class="table-class"
                            >
                                <TableHead class="table_header">
                                    <TableHeadCell>Response</TableHeadCell>
                                </TableHead>
                                <TableBody>
                                    <TableBodyRow>
                                        <TableBodyCell>
                                            <div>
                                                <Label
                                                    for="textarea-id"
                                                    class="mb-2"
                                                    ><span class="blacktext">AI agent response</span></Label
                                                >
                                                <Textarea disabled="disabled"
                                                    id="textarea-id"
                                                    placeholder="No response yet."
                                                    rows={8}
                                                    name="message"
                                                    bind:value={response}
                                                    class="w-full blacktext"
                                                />
                                            </div>
                                        </TableBodyCell>
                                    </TableBodyRow>
                                </TableBody>
                            </Table>
                        </div>
                    </div>
                </div>
            </main>
        </Route>
        <Route path="/logs">
            <Logs />
        </Route>
    </Router>
    <InsecureAppFooter />
</div>
