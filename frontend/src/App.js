import React from "react";
import { BrowserRouter as Router, Routes, Route, NavLink, Navigate } from "react-router-dom";
import BlocksList from "./components/BlocksList";
import TransactionsList from "./components/TransactionsList";
import AccountsList from "./components/AccountsList";
import AddTransactionForm from "./components/AddTransactionForm";
import AddAccountForm from "./components/AddAccountForm";
import MempoolList from "./components/MempoolList";
import SecurityPanel from "./components/SecurityPanel";
import AdminPanel from "./components/AdminPanel";

const navStyle = {
  padding: "8px 18px",
  borderRadius: 6,
  background: "#e0e6ed",
  color: "#333",
  fontWeight: "bold",
  textDecoration: "none",
  fontSize: 16,
  transition: "all 0.2s"
};
const navActive = {
  background: "#2d3a4a",
  color: "#fff"
};

function App() {
  return (
    <Router>
      <div style={{ direction: "rtl", fontFamily: "Vazir, Tahoma, Arial", maxWidth: 800, margin: "0 auto", background: "#f7f7fa", minHeight: "100vh", padding: 24 }}>
        <h1 style={{ textAlign: "center", margin: 30, color: "#2d3a4a", letterSpacing: 1 }}>PersianChain Explorer</h1>
        <nav style={{ display: "flex", justifyContent: "center", gap: 16, marginBottom: 32 }}>
          <NavLink to="/blocks" style={({ isActive }) => isActive ? { ...navStyle, ...navActive } : navStyle}>بلاک‌ها</NavLink>
          <NavLink to="/transactions" style={({ isActive }) => isActive ? { ...navStyle, ...navActive } : navStyle}>تراکنش‌ها</NavLink>
          <NavLink to="/accounts" style={({ isActive }) => isActive ? { ...navStyle, ...navActive } : navStyle}>حساب‌ها</NavLink>
          <NavLink to="/mempool" style={({ isActive }) => isActive ? { ...navStyle, ...navActive } : navStyle}>استخر تراکنش‌ها</NavLink>
          <NavLink to="/security" style={({ isActive }) => isActive ? { ...navStyle, ...navActive } : navStyle}>امنیت و رمزنگاری</NavLink>
          <NavLink to="/admin" style={({ isActive }) => isActive ? { ...navStyle, ...navActive } : navStyle}>مدیریت</NavLink>
        </nav>
        <Routes>
          <Route path="/" element={<Navigate to="/blocks" />} />
          <Route path="/blocks" element={<BlocksList />} />
          <Route path="/transactions" element={<><TransactionsList /><AddTransactionForm /></>} />
          <Route path="/accounts" element={<><AccountsList /><AddAccountForm /></>} />
          <Route path="/mempool" element={<MempoolList />} />
          <Route path="/security" element={<SecurityPanel />} />
          <Route path="/admin" element={<AdminPanel />} />
        </Routes>
        <footer style={{ textAlign: "center", marginTop: 40, color: "#888" }}>
          PersianChain &copy; {new Date().getFullYear()} | Mohammad Nasser Haji Hashemabad
        </footer>
      </div>
    </Router>
  );
}

export default App; 