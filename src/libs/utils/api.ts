// Type definitions for log entries and API responses

export interface LogEntry {
	timestamp: string;
	user_input: string;
	system_prompt?: string;
	response: string;
	risk_score: number;
}

// Fetch chat logs from the backend
export async function fetchLogs(): Promise<LogEntry[]> {
	const res = await fetch('http://0.0.0.0:5001/logs');
	if (!res.ok) {
		throw new Error(`Failed to fetch logs: ${res.statusText}`);
	}
	return await res.json();
}
