import React, { useState } from "react";

async function encryptData(data) {
  const res = await fetch("http://localhost:8000/blockchain/security/encrypt", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ data }),
  });
  return res.json();
}

async function decryptData(encrypted) {
  const res = await fetch("http://localhost:8000/blockchain/security/decrypt", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ encrypted }),
  });
  return res.json();
}

async function checkDoubleSpend(tx) {
  const res = await fetch("http://localhost:8000/blockchain/security/double_spend", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(tx),
  });
  return res.json();
}

export default function SecurityPanel() {
  const [data, setData] = useState("");
  const [encrypted, setEncrypted] = useState("");
  const [decrypted, setDecrypted] = useState("");
  const [tx, setTx] = useState({ فرستنده: "", گیرنده: "", مقدار: "" });
  const [doubleSpendResult, setDoubleSpendResult] = useState("");
  const [key, setKey] = useState("");

  const handleEncrypt = async (e) => {
    e.preventDefault();
    const res = await encryptData(data);
    setEncrypted(res.encrypted || "");
    setKey(res.key || "");
    setDecrypted("");
  };

  const handleDecrypt = async (e) => {
    e.preventDefault();
    const res = await decryptData(encrypted);
    setDecrypted(res.decrypted || res.error || "");
  };

  const handleDoubleSpend = async (e) => {
    e.preventDefault();
    const res = await checkDoubleSpend({ ...tx, مقدار: Number(tx.مقدار) });
    setDoubleSpendResult(res.is_unique ? "تراکنش یکتا است." : "تراکنش تکراری است!");
  };

  return (
    <div style={{ marginTop: 40, padding: 20, border: "1px solid #aaa", borderRadius: 8 }}>
      <h3>امنیت و رمزنگاری</h3>
      <form onSubmit={handleEncrypt} style={{ marginBottom: 10 }}>
        <label>داده برای رمزنگاری: </label>
        <input value={data} onChange={e => setData(e.target.value)} />
        <button type="submit">رمزنگاری</button>
      </form>
      {encrypted && (
        <div>
          <div>داده رمزنگاری شده: <span style={{ fontFamily: "monospace" }}>{encrypted}</span></div>
          <div>کلید: <span style={{ fontFamily: "monospace" }}>{key}</span></div>
        </div>
      )}
      <form onSubmit={handleDecrypt} style={{ margin: "10px 0" }}>
        <label>داده رمزنگاری شده: </label>
        <input value={encrypted} onChange={e => setEncrypted(e.target.value)} />
        <button type="submit">رمزگشایی</button>
      </form>
      {decrypted && <div>داده رمزگشایی شده: <span style={{ fontFamily: "monospace" }}>{decrypted}</span></div>}
      <hr />
      <form onSubmit={handleDoubleSpend} style={{ marginTop: 10 }}>
        <h4>بررسی دوبار خرج کردن</h4>
        <div>
          <label>فرستنده: </label>
          <input value={tx.فرستنده} onChange={e => setTx({ ...tx, فرستنده: e.target.value })} />
        </div>
        <div>
          <label>گیرنده: </label>
          <input value={tx.گیرنده} onChange={e => setTx({ ...tx, گیرنده: e.target.value })} />
        </div>
        <div>
          <label>مقدار: </label>
          <input type="number" value={tx.مقدار} onChange={e => setTx({ ...tx, مقدار: e.target.value })} />
        </div>
        <button type="submit">بررسی یکتایی تراکنش</button>
      </form>
      {doubleSpendResult && <div style={{ color: doubleSpendResult.includes("تکراری") ? "red" : "green" }}>{doubleSpendResult}</div>}
    </div>
  );
} 