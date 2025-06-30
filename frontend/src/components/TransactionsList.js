import React, { useEffect, useState } from "react";
import { fetchTransactions } from "../api/api";

export default function TransactionsList() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    fetchTransactions().then(setTransactions);
  }, []);

  return (
    <div>
      <h2>لیست تراکنش‌ها</h2>
      <ul>
        {transactions.map((tx, idx) => (
          <li key={idx} style={{ marginBottom: 8, borderBottom: "1px solid #eee" }}>
            <b>فرستنده:</b> {tx.فرستنده} | <b>گیرنده:</b> {tx.گیرنده} | <b>مقدار:</b> {tx.مقدار}
          </li>
        ))}
      </ul>
    </div>
  );
} 