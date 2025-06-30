const API_BASE = "http://localhost:8000/blockchain";

export async function fetchBlocks() {
  const res = await fetch(`${API_BASE}/blocks`);
  return res.json();
}

export async function fetchTransactions() {
  const res = await fetch(`${API_BASE}/transactions`);
  return res.json();
}

export async function addTransaction(data) {
  const res = await fetch(`${API_BASE}/transactions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function fetchAccounts() {
  const res = await fetch(`${API_BASE}/accounts`);
  return res.json();
}

export async function addAccount(data) {
  const res = await fetch(`${API_BASE}/accounts`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
} 