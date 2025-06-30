import React, { useEffect, useState } from "react";

async function fetchBlocks() {
  const res = await fetch("http://localhost:8000/blockchain/blocks");
  return res.json();
}
async function fetchTransactions() {
  const res = await fetch("http://localhost:8000/blockchain/transactions");
  return res.json();
}
async function fetchAccounts() {
  const res = await fetch("http://localhost:8000/blockchain/accounts");
  return res.json();
}
async function clearMempool() {
  // فرض: endpoint پاکسازی استخر به صورت POST /blockchain/mempool/clear
  const res = await fetch("http://localhost:8000/blockchain/mempool/clear", { method: "POST" });
  return res.json();
}

export default function AdminPanel() {
  const [counts, setCounts] = useState({ blocks: 0, transactions: 0, accounts: 0 });
  const [پیام, setپیام] = useState("");

  const loadStats = async () => {
    const [blocks, txs, accs] = await Promise.all([
      fetchBlocks(), fetchTransactions(), fetchAccounts()
    ]);
    setCounts({
      blocks: blocks.length,
      transactions: txs.length,
      accounts: Object.keys(accs).length
    });
  };

  useEffect(() => {
    loadStats();
  }, []);

  const handleClearMempool = async () => {
    const res = await clearMempool();
    setپیام(res.message || "استخر تراکنش‌ها پاک شد.");
  };

  return (
    <div style={{ margin: "32px 0", padding: 20, border: "1px solid #bbb", borderRadius: 8, background: "#fffbe7" }}>
      <h3>بخش مدیریتی بلاکچین</h3>
      <div>تعداد کل بلاک‌ها: <b>{counts.blocks}</b></div>
      <div>تعداد کل تراکنش‌ها: <b>{counts.transactions}</b></div>
      <div>تعداد کل حساب‌ها: <b>{counts.accounts}</b></div>
      <button onClick={handleClearMempool} style={{ marginTop: 16, padding: "8px 18px", borderRadius: 6, background: "#e74c3c", color: "#fff", border: "none", fontWeight: "bold", cursor: "pointer" }}>
        پاکسازی استخر تراکنش‌ها
      </button>
      {پیام && <div style={{ color: "green", marginTop: 10 }}>{پیام}</div>}
    </div>
  );
} 