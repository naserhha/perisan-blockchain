# PersianChain

[English below | توضیحات فارسی در ادامه]

---

## معرفی پروژه (فارسی)

**PersianChain** یک بلاکچین آموزشی و ماژولار به زبان فارسی است که با هدف آموزش مفاهیم اصلی بلاکچین، رمزنگاری، اجماع و شبکه همتا به همتا طراحی شده است. تمامی کدها، متغیرها و مستندات به زبان فارسی و با ساختار ماژولار پیاده‌سازی شده‌اند تا توسعه و یادگیری را برای فارسی‌زبانان ساده‌تر کند.

### ویژگی‌ها
- هسته بلاکچین با امضای دیجیتال و رمزنگاری کلید عمومی-خصوصی
- شبکه همتا به همتا (P2P) برای ارتباط بین نودها
- استخر تراکنش‌های تاییدنشده (Mempool)
- مدیریت و تخصیص کارمزد تراکنش‌ها
- الگوریتم اجماع اثبات سهام (PoS)
- مدیریت حساب‌ها و موجودی کاربران
- بلاک اکسپلورر و API ساده با Flask
- مدیریت فورک و انتخاب زنجیره معتبرتر
- تست واحد (Unit Test) برای بخش‌های اصلی
- ماژول امنیت و رمزنگاری داده‌های حساس و مقابله با دوبار خرج کردن

### ساختار ماژولار
هر قابلیت در یک فایل جداگانه پیاده‌سازی شده و به راحتی قابل توسعه و اتصال به یکدیگر است.

### نصب پیش‌نیازها

```bash
pip install flask ecdsa cryptography
```

### اجرای بلاک اکسپلورر و API

```bash
python explorer_api.py
```

### اجرای تست واحد

```bash
python test_persianchain.py
```

### اطلاعات نویسنده

- Mohammad Nasser Haji Hashemabad
- [LinkedIn](https://ir.linkedin.com/in/nasserhaji)
- [GitHub](https://github.com/nasserhaji)
- [Website](https://mohammadnasser.com/)

---

## Project Introduction (English)

**PersianChain** is an educational and modular blockchain project in Persian (Farsi), designed to teach the core concepts of blockchain, cryptography, consensus, and peer-to-peer networking. All code, variables, and documentation are in Persian, making it ideal for Farsi-speaking learners and developers.

### Features
- Blockchain core with digital signature and public/private key cryptography
- Peer-to-peer (P2P) networking between nodes
- Mempool for unconfirmed transactions
- Transaction fee management and allocation
- Proof of Stake (PoS) consensus algorithm
- Account and balance management
- Simple block explorer and API with Flask
- Fork management and longest chain selection
- Unit tests for main modules
- Security module for sensitive data encryption and double-spending prevention

### Modular Structure
Each feature is implemented in a separate file/module, making the project easy to extend and integrate.

### Requirements

```bash
pip install flask ecdsa cryptography
```

### Run Block Explorer & API

```bash
python explorer_api.py
```

### Run Unit Tests

```bash
python test_persianchain.py
```

### Author

- Mohammad Nasser Haji Hashemabad
- [LinkedIn](https://ir.linkedin.com/in/nasserhaji)
- [GitHub](https://github.com/nasserhaji)
- [Website](https://mohammadnasser.com/) 