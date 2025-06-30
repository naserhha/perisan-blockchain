# PersianChain

> **یک بلاکچین آموزشی و ماژولار به زبان فارسی با پشتیبانی از قرارداد هوشمند**

---

## مقدمه

**PersianChain** یک پروژه بلاکچین متن‌باز و آموزشی است که با هدف آموزش مفاهیم پایه و پیشرفته بلاکچین، رمزنگاری، اجماع، شبکه همتا به همتا و قرارداد هوشمند به زبان فارسی توسعه یافته است. این پروژه با ساختار ماژولار و مستندات کامل، بستری مناسب برای یادگیری، توسعه و آزمایش ایده‌های بلاکچینی برای فارسی‌زبانان فراهم می‌کند.

---

## معماری و ساختار پروژه

- **Backend:** پیاده‌سازی هسته بلاکچین، اجماع، مدیریت حساب، استخر تراکنش، امنیت و قرارداد هوشمند با Python و FastAPI
- **Frontend:** داشبورد مدیریتی و بلاک اکسپلورر با React و React Router
- **ساختار ماژولار:** هر قابلیت (بلاکچین، حساب، تراکنش، mempool، اجماع، امنیت، قرارداد هوشمند و...) در یک ماژول جداگانه

### ساختار پوشه‌ها
```
perisan-blockchain/
  backend/
    main.py
    api/
      blockchain.py
      accounts.py
      transactions.py
      mempool.py
      fee.py
      consensus.py
      security.py
      smart_contract.py
      ...
  smart_contract.py
  ...
  frontend/
    src/
      components/
        ...
      api/
        api.js
      App.js
      ...
```

---

## راه‌اندازی سریع

### پیش‌نیازها
- Python 3.8+
- Node.js 16+

### نصب Backend
```bash
pip install fastapi uvicorn flask ecdsa cryptography
```

### نصب Frontend
```bash
cd frontend
npm install
npm install react-router-dom chart.js react-chartjs-2
```

### اجرای Backend
```bash
uvicorn backend.main:app --reload
```

### اجرای Frontend
```bash
cd frontend
npm start
```

### اجرای تست واحد
```bash
python test_persianchain.py
```

---

## مستندات API

### بلاکچین
- `GET /blockchain/blocks` — دریافت لیست بلاک‌ها
- `GET /blockchain/transactions` — دریافت لیست تراکنش‌ها
- `POST /blockchain/transactions` — افزودن تراکنش جدید
- `GET /blockchain/accounts` — دریافت لیست حساب‌ها
- `POST /blockchain/accounts` — افزودن حساب جدید
- `GET /blockchain/mempool` — مشاهده استخر تراکنش‌ها
- `POST /blockchain/mempool` — افزودن تراکنش به استخر
- `POST /blockchain/mempool/clear` — پاکسازی استخر تراکنش‌ها

### امنیت و رمزنگاری
- `POST /blockchain/security/encrypt` — رمزنگاری داده
- `POST /blockchain/security/decrypt` — رمزگشایی داده
- `POST /blockchain/security/double_spend` — بررسی دوبار خرج کردن

### قرارداد هوشمند
- `POST /blockchain/smartcontract/register` — ثبت قرارداد جدید (body: نام سازنده)
- `GET /blockchain/smartcontract/list` — لیست قراردادها
- `POST /blockchain/smartcontract/execute/{id}` — اجرای قرارداد (body: پارامترهای ورودی)

---

## مثال استفاده از قرارداد هوشمند

### ثبت قرارداد جدید
```http
POST /blockchain/smartcontract/register
Content-Type: application/json

"سازنده۱"
```

### لیست قراردادها
```http
GET /blockchain/smartcontract/list
```

### اجرای قرارداد (جمع دو عدد)
```http
POST /blockchain/smartcontract/execute/1
Content-Type: application/json

{
  "a": 5,
  "b": 7
}
```
خروجی:
```json
{
  "خروجی": 12,
  "وضعیت": {"آخرین_جمع": 12}
}
```

---

## توسعه و مشارکت

- کدها و مستندات کاملاً فارسی و قابل توسعه هستند.
- برای افزودن قرارداد هوشمند جدید، کافی است یک تابع پایتونی با امضای `(وضعیت, ورودی)` بنویسید و آن را به مدیریت قراردادها اضافه کنید.
- برای توسعه frontend، کامپوننت‌های React را گسترش دهید یا صفحات جدید بسازید.
- تست‌های واحد و یکپارچه را با `python test_persianchain.py` اجرا کنید.

### مشارکت
- Pull Request و Issueهای شما برای بهبود پروژه بسیار ارزشمند است.
- لطفاً قبل از ارسال PR، تست‌ها را اجرا و مستندات را به‌روزرسانی کنید.

---

## نویسنده و ارتباط

- Mohammad Nasser Haji Hashemabad محمد ناصر حاجی هاشم آباد
- [LinkedIn](https://ir.linkedin.com/in/nasserhaji)
- [GitHub](https://github.com/nasserhaji)
- [Website](https://mohammadnasser.com/)

---

## English Summary

**PersianChain** is a modular, open-source educational blockchain in Persian, featuring digital signature, P2P, mempool, PoS, security, and smart contract support. The project is fully documented and ready for extension and experimentation.

- Backend: Python (FastAPI)
- Frontend: React (SPA)
- Smart contract API: Register, list, and execute contracts
- All code and docs in Persian for Farsi-speaking learners

---

> برای هرگونه سوال یا همکاری، از طریق لینکدین یا گیت‌هاب با من در ارتباط باشید. 
