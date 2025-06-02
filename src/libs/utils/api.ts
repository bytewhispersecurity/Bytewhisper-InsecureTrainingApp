// Type definitions for log entries and API responses

export interface LogEntry {
	timestamp: string;
	user_input: string;
	system_prompt?: string;
	response: string;
	risk_score: number;
}

export interface ScanResponse {
	response?: string;
	error?: string;
	risk_score: number;
}

// Send user input to the backend along with the current mode
export async function sendQuery(query: string, mode: 'secure' | 'vulnerable' = 'secure'): Promise<ScanResponse> {
	const res = await fetch('http://0.0.0.0:5001/scan', {
		method: 'POST',
		mode: 'cors',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ query, mode })
	});

	if (!res.ok) {
		throw new Error(`Failed to send query: ${res.statusText}`);
	}

	return await res.json();
}

// Fetch chat logs from the backend
export async function fetchLogs(): Promise<LogEntry[]> {
	const res = await fetch('http://0.0.0.0:5001/logs');
	if (!res.ok) {
		throw new Error(`Failed to fetch logs: ${res.statusText}`);
	}
	return await res.json();
}
