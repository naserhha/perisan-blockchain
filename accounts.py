/**
 * Project: Perisan Blockchain
 * Author: Mohammad Nasser Haji Hashemabad
 * License: Custom NonCommercial Attribution License (v1.0 - July 2025)
 * Website: https://mohammadnasser.com
 * Email: info@mohammadnasser.com
 *
 * This code is free for non-commercial use only.
 * Commercial use, redistribution, or monetization requires written permission.
 */

# ماژول مدیریت وضعیت حساب‌ها و موجودی برای PersianChain
# نویسنده: Mohammad Nasser Haji Hashemabad
# توضیحات: این ماژول مدیریت حساب‌ها و موجودی کاربران را انجام می‌دهد.

class مدیریت_حساب:
    def __init__(self):
        self.حساب_ها = {}  # {آدرس: موجودی}

    def افزودن_حساب(self, آدرس, مقدار_اولیه=0):
        if آدرس not in self.حساب_ها:
            self.حساب_ها[آدرس] = مقدار_اولیه
            return True
        return False

    def دریافت_موجودی(self, آدرس):
        return self.حساب_ها.get(آدرس, 0)

    def به_روزرسانی_موجودی(self, آدرس, مقدار):
        if آدرس in self.حساب_ها:
            self.حساب_ها[آدرس] += مقدار
            return True
        return False

    def انتقال(self, فرستنده, گیرنده, مقدار):
        if self.دریافت_موجودی(فرستنده) >= مقدار:
            self.به_روزرسانی_موجودی(فرستنده, -مقدار)
            self.افزودن_حساب(گیرنده)
            self.به_روزرسانی_موجودی(گیرنده, مقدار)
            return True
        return False

    def لیست_حساب_ها(self):
        return dict(self.حساب_ها)

# نمونه استفاده
if __name__ == "__main__":
    حساب = مدیریت_حساب()
    حساب.افزودن_حساب('A', 100)
    حساب.افزودن_حساب('B', 50)
    print("موجودی A:", حساب.دریافت_موجودی('A'))
    print("انتقال 30 از A به B:", حساب.انتقال('A', 'B', 30))
    print("موجودی A:", حساب.دریافت_موجودی('A'))
    print("موجودی B:", حساب.دریافت_موجودی('B'))
    print("لیست حساب‌ها:", حساب.لیست_حساب_ها()) 
