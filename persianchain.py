# نام پروژه: PersianChain
# نام فایل: persianchain.py
# نویسنده: Mohammad Nasser Haji Hashemabad
# لینکدین: https://ir.linkedin.com/in/naserhha
# گیت‌هاب: https://github.com/naserhha
# وب‌سایت: https://mohammadnasser.com/ 
# بلاکچین ساده به زبان فارسی
# توضیحات: این کد یک بلاکچین ساده شبیه بیت‌کوین را با متغیرها و توضیحات کاملاً فارسی پیاده‌سازی می‌کند.

import hashlib
import time
import ecdsa
import binascii

# --- بخش ۱: امضای دیجیتال و رمزنگاری کلید عمومی-خصوصی ---
# برای نصب کتابخانه ecdsa:
# pip install ecdsa

# کلاس کاربر با کلید خصوصی و عمومی
class کاربر:
    def __init__(self):
        self.کلید_خصوصی = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.کلید_عمومی = self.کلید_خصوصی.get_verifying_key()

    def دریافت_آدرس(self):
        # آدرس کاربر را با هش کلید عمومی تولید می‌کنیم
        return binascii.hexlify(self.کلید_عمومی.to_string()).decode()

    def امضای_پیام(self, پیام):
        return binascii.hexlify(self.کلید_خصوصی.sign(پیام.encode())).decode()

    def دریافت_کلید_عمومی(self):
        return binascii.hexlify(self.کلید_عمومی.to_string()).decode()

# تابع اعتبارسنجی امضا
def اعتبارسنجی_امضا(کلید_عمومی_متنی, پیام, امضا):
    کلید_عمومی = ecdsa.VerifyingKey.from_string(binascii.unhexlify(کلید_عمومی_متنی), curve=ecdsa.SECP256k1)
    try:
        نتیجه = کلید_عمومی.verify(binascii.unhexlify(امضا), پیام.encode())
        return نتیجه
    except:
        return False

# تعریف کلاس تراکنش
class تراکنش:
    def __init__(self, فرستنده, گیرنده, مقدار, امضا=None, کلید_عمومی_فرستنده=None, کارمزد=0):
        self.فرستنده = فرستنده
        self.گیرنده = گیرنده
        self.مقدار = مقدار
        self.کارمزد = کارمزد
        self.امضا = امضا
        self.کلید_عمومی_فرستنده = کلید_عمومی_فرستنده

    def تولید_داده_تراکنش(self):
        return f"{self.فرستنده}:{self.گیرنده}:{self.مقدار}:{self.کارمزد}"

    def امضا_تراکنش(self, کلید_خصوصی_فرستنده):
        داده = self.تولید_داده_تراکنش()
        امضا = binascii.hexlify(کلید_خصوصی_فرستنده.sign(داده.encode())).decode()
        self.امضا = امضا
        self.کلید_عمومی_فرستنده = binascii.hexlify(کلید_خصوصی_فرستنده.get_verifying_key().to_string()).decode()

    def اعتبار_تراکنش(self):
        if self.فرستنده == "سیستم":
            return True  # تراکنش پاداش نیازی به امضا ندارد
        if not self.امضا or not self.کلید_عمومی_فرستنده:
            return False
        کلید_عمومی = ecdsa.VerifyingKey.from_string(binascii.unhexlify(self.کلید_عمومی_فرستنده), curve=ecdsa.SECP256k1)
        try:
            داده = self.تولید_داده_تراکنش()
            return کلید_عمومی.verify(binascii.unhexlify(self.امضا), داده.encode())
        except:
            return False

    def __repr__(self):
        return f"تراکنش(فرستنده={self.فرستنده}, گیرنده={self.گیرنده}, مقدار={self.مقدار}, کارمزد={self.کارمزد})"

# تعریف کلاس بلاک
class بلاک:
    def __init__(self, شماره, تراکنش_ها, هش_قبلی, زمان_ایجاد=None, عدد_تصادفی=0):
        self.شماره = شماره
        self.تراکنش_ها = تراکنش_ها
        self.هش_قبلی = هش_قبلی
        self.زمان_ایجاد = زمان_ایجاد or time.time()
        self.عدد_تصادفی = عدد_تصادفی
        self.هش = self.محاسبه_هش()

    def محاسبه_هش(self):
        رشته = str(self.شماره) + str(self.تراکنش_ها) + str(self.هش_قبلی) + str(self.زمان_ایجاد) + str(self.عدد_تصادفی)
        return hashlib.sha256(رشته.encode()).hexdigest()

    def __repr__(self):
        return f"بلاک(شماره={self.شماره}, هش={self.هش[:10]}..., تراکنش_ها={self.تراکنش_ها})"

# تعریف کلاس بلاکچین
class بلاکچین:
    def __init__(self):
        self.زنجیره = []
        self.تراکنش_های_در_انتظار = []
        self.سختی = 3  # تعداد صفرهای ابتدایی برای اثبات کار
        self.ایجاد_بلاک_اولیه()

    def ایجاد_بلاک_اولیه(self):
        بلاک_اولیه = بلاک(0, [], "0")
        self.زنجیره.append(بلاک_اولیه)

    def افزودن_تراکنش(self, تراکنش):
        self.تراکنش_های_در_انتظار.append(تراکنش)

    def استخراج_بلاک(self, پاداش_استخراج_کننده):
        # افزودن تراکنش پاداش
        تراکنش_پاداش = تراکنش("سیستم", پاداش_استخراج_کننده, 1)
        تراکنش_ها = self.تراکنش_های_در_انتظار + [تراکنش_پاداش]
        بلاک_جدید = بلاک(
            شماره=len(self.زنجیره),
            تراکنش_ها=تراکنش_ها,
            هش_قبلی=self.زنجیره[-1].هش
        )
        بلاک_جدید = self.اثبات_کار(بلاک_جدید)
        self.زنجیره.append(بلاک_جدید)
        self.تراکنش_های_در_انتظار = []
        return بلاک_جدید

    def اثبات_کار(self, بلاک):
        while not بلاک.هش.startswith("0" * self.سختی):
            بلاک.عدد_تصادفی += 1
            بلاک.هش = بلاک.محاسبه_هش()
        return بلاک

    def اعتبار_زنجیره(self):
        for i in range(1, len(self.زنجیره)):
            بلاک_فعلی = self.زنجیره[i]
            بلاک_قبلی = self.زنجیره[i-1]
            if بلاک_فعلی.هش != بلاک_فعلی.محاسبه_هش():
                return False
            if بلاک_فعلی.هش_قبلی != بلاک_قبلی.هش:
                return False
        return True

    def نمایش_زنجیره(self):
        for بلاک_در_زنجیره in self.زنجیره:
            print(بلاک_در_زنجیره)

# نمونه استفاده از بلاکچین
if __name__ == "__main__":
    زنجیره_من = بلاکچین()
    print("افزودن تراکنش‌ها...")
    زنجیره_من.افزودن_تراکنش(تراکنش("علی", "رضا", 5))
    زنجیره_من.افزودن_تراکنش(تراکنش("رضا", "مریم", 2))
    print("استخراج بلاک توسط 'مهدی'...")
    بلاک_جدید = زنجیره_من.استخراج_بلاک("مهدی")
    print("بلاک جدید:", بلاک_جدید)
    print("اعتبار زنجیره:", "معتبر" if زنجیره_من.اعتبار_زنجیره() else "نامعتبر")
    print("نمایش کل زنجیره:")
    زنجیره_من.نمایش_زنجیره()

    print("--- نمونه تولید کلید و امضای تراکنش ---")
    کاربر۱ = کاربر()
    کاربر۲ = کاربر()
    آدرس۱ = کاربر۱.دریافت_آدرس()
    آدرس۲ = کاربر۲.دریافت_آدرس()
    تراکنش۱ = تراکنش(آدرس۱, آدرس۲, 10, کارمزد=1)
    تراکنش۱.امضا_تراکنش(کاربر۱.کلید_خصوصی)
    print("آدرس فرستنده:", آدرس۱)
    print("آدرس گیرنده:", آدرس۲)
    print("امضا:", تراکنش۱.امضا)
    print("اعتبارسنجی امضا:", "معتبر" if تراکنش۱.اعتبار_تراکنش() else "نامعتبر") 