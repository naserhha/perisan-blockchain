import React, { useEffect, useState } from "react";
import { Bar, Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, ArcElement, Tooltip, Legend);

async function fetchBlocks() {
  const res = await fetch("http://localhost:8000/blockchain/blocks");
  return res.json();
}
async function fetchAccounts() {
  const res = await fetch("http://localhost:8000/blockchain/accounts");
  return res.json();
}

export default function ReportPanel() {
  const [blocks, setBlocks] = useState([]);
  const [accounts, setAccounts] = useState({});

  useEffect(() => {
    fetchBlocks().then(setBlocks);
    fetchAccounts().then(setAccounts);
  }, []);

  // داده نمودار تعداد تراکنش‌ها در هر بلاک
  const txPerBlockData = {
    labels: blocks.map(b => `بلاک ${b.شماره}`),
    datasets: [
      {
        label: "تعداد تراکنش‌ها",
        data: blocks.map(b => (b.تراکنش_ها ? b.تراکنش_ها.length : 0)),
        backgroundColor: "#2d3a4a"
      }
    ]
  };

  // داده نمودار توزیع موجودی حساب‌ها
  const accLabels = Object.keys(accounts);
  const accBalances = accLabels.map(a => accounts[a]);
  const accColors = accLabels.map((_, i) => `hsl(${i * 40}, 70%, 60%)`);
  const accDistData = {
    labels: accLabels,
    datasets: [
      {
        label: "موجودی",
        data: accBalances,
        backgroundColor: accColors
      }
    ]
  };

  return (
    <div style={{ margin: "32px 0", padding: 20, border: "1px solid #bbb", borderRadius: 8, background: "#f0f7ff" }}>
      <h3>گزارش‌گیری و آمار بلاکچین</h3>
      <div style={{ marginBottom: 32 }}>
        <h4>تعداد تراکنش‌ها در هر بلاک</h4>
        {blocks.length > 0 ? (
          <Bar data={txPerBlockData} options={{ plugins: { legend: { display: false } } }} />
        ) : (
          <div>داده‌ای برای نمایش وجود ندارد.</div>
        )}
      </div>
      <div>
        <h4>توزیع موجودی حساب‌ها</h4>
        {accLabels.length > 0 ? (
          <Pie data={accDistData} />
        ) : (
          <div>داده‌ای برای نمایش وجود ندارد.</div>
        )}
      </div>
    </div>
  );
} 