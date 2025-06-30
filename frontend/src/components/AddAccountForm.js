import React, { useState } from "react";
import { addAccount } from "../api/api";

export default function AddAccountForm() {
  const [آدرس, setآدرس] = useState("");
  const [مقدار, setمقدار] = useState("");
  const [پیام, setپیام] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!آدرس) {
      setپیام("آدرس را وارد کنید.");
      return;
    }
    const result = await addAccount({ آدرس, مقدار: Number(مقدار) });
    setپیام(result.message || "حساب افزوده شد.");
    setآدرس("");
    setمقدار("");
  };

  return (
    <div style={{ marginTop: 30 }}>
      <h3>افزودن حساب جدید</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label>آدرس: </label>
          <input value={آدرس} onChange={e => setآدرس(e.target.value)} />
        </div>
        <div>
          <label>مقدار اولیه: </label>
          <input type="number" value={مقدار} onChange={e => setمقدار(e.target.value)} />
        </div>
        <button type="submit">افزودن حساب</button>
      </form>
      {پیام && <div style={{ color: "green", marginTop: 10 }}>{پیام}</div>}
    </div>
  );
} 