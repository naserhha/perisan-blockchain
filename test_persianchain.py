# ماژول تست واحد برای PersianChain
# نویسنده: Mohammad Nasser Haji Hashemabad
# توضیحات: این فایل تست بخش‌های اصلی پروژه را با unittest انجام می‌دهد.
import unittest
from accounts import مدیریت_حساب
from mempool import استخر_تراکنش
from fork_manager import مدیریت_فورک

class تست_مدیریت_حساب(unittest.TestCase):
    def test_افزودن_و_انتقال(self):
        حساب = مدیریت_حساب()
        حساب.افزودن_حساب('A', 100)
        حساب.افزودن_حساب('B', 0)
        self.assertEqual(حساب.دریافت_موجودی('A'), 100)
        self.assertTrue(حساب.انتقال('A', 'B', 30))
        self.assertEqual(حساب.دریافت_موجودی('A'), 70)
        self.assertEqual(حساب.دریافت_موجودی('B'), 30)

class تست_استخر_تراکنش(unittest.TestCase):
    def test_افزودن_و_حذف(self):
        استخر = استخر_تراکنش()
        تراکنش = {"فرستنده": "A", "گیرنده": "B", "مقدار": 10}
        self.assertTrue(استخر.افزودن_تراکنش(تراکنش))
        self.assertIn(تراکنش, استخر.دریافت_همه())
        self.assertTrue(استخر.حذف_تراکنش(تراکنش))
        self.assertNotIn(تراکنش, استخر.دریافت_همه())

class تست_مدیریت_فورک(unittest.TestCase):
    def test_انتخاب_زنجیره_بلندتر(self):
        زنجیره۱ = [1, 2, 3]
        زنجیره۲ = [1, 2, 3, 4]
        فورک = مدیریت_فورک(زنجیره۱)
        فورک.به_روزرسانی_زنجیره(زنجیره۲)
        self.assertEqual(فورک.زنجیره_فعلی, زنجیره۲)

if __name__ == "__main__":
    unittest.main() 