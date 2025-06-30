import React, { useState } from "react";
import { addTransaction } from "../api/api";

export default function AddTransactionForm() {
  const [فرستنده, setفرستنده] = useState("");
  const [گیرنده, setگیرنده] = useState("");
  const [مقدار, setمقدار] = useState("");
  const [پیام, setپیام] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!فرستنده || !گیرنده || !مقدار) {
      setپیام("لطفاً همه فیلدها را پر کنید.");
      return;
    }
    const result = await addTransaction({ فرستنده, گیرنده, مقدار: Number(مقدار) });
    setپیام(result.message || "تراکنش ارسال شد.");
    setفرستنده("");
    setگیرنده("");
    setمقدار("");
  };

  return (
    <div style={{ marginTop: 30 }}>
      <h3>افزودن تراکنش جدید</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label>فرستنده: </label>
          <input value={فرستنده} onChange={e => setفرستنده(e.target.value)} />
        </div>
        <div>
          <label>گیرنده: </label>
          <input value={گیرنده} onChange={e => setگیرنده(e.target.value)} />
        </div>
        <div>
          <label>مقدار: </label>
          <input type="number" value={مقدار} onChange={e => setمقدار(e.target.value)} />
        </div>
        <button type="submit">ارسال تراکنش</button>
      </form>
      {پیام && <div style={{ color: "green", marginTop: 10 }}>{پیام}</div>}
    </div>
  );
} 