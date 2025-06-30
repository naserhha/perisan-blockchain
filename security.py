# ماژول امنیت و رمزنگاری داده‌های حساس برای PersianChain
# نویسنده: Mohammad Nasser Haji Hashemabad
# توضیحات: این ماژول رمزنگاری داده، تولید هش امن و مقابله با حمله دوبار خرج کردن را فراهم می‌کند.
# برای اجرا: pip install cryptography

from cryptography.fernet import Fernet
import hashlib

class رمزنگاری:
    def __init__(self, کلید=None):
        self.کلید = کلید or Fernet.generate_key()
        self.ابزار = Fernet(self.کلید)

    def رمزنگاری_داده(self, داده):
        return self.ابزار.encrypt(dada.encode()).decode()

    def رمزگشایی_داده(self, داده_رمزنگاری):
        return self.ابزار.decrypt(dada_رمزنگاری.encode()).decode()

    def دریافت_کلید(self):
        return self.کلید.decode()

# تابع تولید هش امن
def هش_امن(داده):
    return hashlib.sha256(داده.encode()).hexdigest()

# مقابله با حمله دوبار خرج کردن
class مقابله_دوبار_خرج:
    def __init__(self):
        self.شناسه_تراکنش_ها = set()

    def بررسی_تراکنش(self, تراکنش):
        شناسه = هش_امن(str(تراکنش))
        if شناسه in self.شناسه_تراکنش_ها:
            return False  # تراکنش تکراری است
        self.شناسه_تراکنش_ها.add(شناسه)
        return True

# نمونه استفاده
if __name__ == "__main__":
    # رمزنگاری و رمزگشایی داده
    رمز = رمزنگاری()
    متن = "داده حساس"
    رمزنگاری_شده = رمز.رمزنگاری_داده(متن)
    print("داده رمزنگاری شده:", رمزنگاری_شده)
    print("داده رمزگشایی شده:", رمز.رمزگشایی_داده(رمزنگاری_شده))
    # تولید هش امن
    print("هش امن داده:", هش_امن(متن))
    # مقابله با دوبار خرج کردن
    مقابله = مقابله_دوبار_خرج()
    تراکنش = {"فرستنده": "A", "گیرنده": "B", "مقدار": 10}
    print("اولین بررسی:", مقابله.بررسی_تراکنش(تراکنش))
    print("بررسی مجدد (باید False باشد):", مقابله.بررسی_تراکنش(تراکنش)) 