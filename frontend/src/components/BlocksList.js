import React, { useEffect, useState } from "react";
import { fetchBlocks } from "../api/api";

export default function BlocksList() {
  const [blocks, setBlocks] = useState([]);

  useEffect(() => {
    fetchBlocks().then(setBlocks);
  }, []);

  return (
    <div>
      <h2>لیست بلاک‌ها</h2>
      <ul>
        {blocks.map((block, idx) => (
          <li key={idx} style={{ marginBottom: 10, borderBottom: "1px solid #ccc" }}>
            <b>شماره:</b> {block.شماره} | <b>هش:</b> {block.هش}
            <br />
            <b>تراکنش‌ها:</b> {JSON.stringify(block.تراکنش_ها)}
          </li>
        ))}
      </ul>
    </div>
  );
} 