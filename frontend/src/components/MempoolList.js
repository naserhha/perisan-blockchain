import React, { useEffect, useState } from "react";

// تابع دریافت استخر تراکنش‌ها
async function getMempool() {
  const res = await fetch("http://localhost:8000/blockchain/mempool");
  return res.json();
}

export default function MempoolList() {
  const [mempool, setMempool] = useState([]);

  useEffect(() => {
    getMempool().then(setMempool);
  }, []);

  return (
    <div>
      <h2>استخر تراکنش‌ها (Mempool)</h2>
      <ul>
        {mempool.map((tx, idx) => (
          <li key={idx} style={{ marginBottom: 8, borderBottom: "1px solid #eee" }}>
            <b>فرستنده:</b> {tx.فرستنده} | <b>گیرنده:</b> {tx.گیرنده} | <b>مقدار:</b> {tx.مقدار}
          </li>
        ))}
      </ul>
    </div>
  );
} 