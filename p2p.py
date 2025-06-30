# ماژول شبکه همتا به همتا (P2P) برای PersianChain
# نویسنده: Mohammad Nasser Haji Hashemabad
# توضیحات: این ماژول امکان ارتباط بین نودهای بلاکچین را فراهم می‌کند.

import socket
import threading
import json

کدگذاری = 'utf-8'

class نود:
    def __init__(self, پورت, نودهای_همسایه=None):
        self.پورت = پورت
        self.نودهای_همسایه = نودهای_همسایه or []  # [(آدرس, پورت)]
        self.زنجیره = None  # باید به نمونه بلاکچین متصل شود
        self.سرور = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.سرور.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.سرور.bind(('0.0.0.0', self.پورت))
        self.سرور.listen(5)
        threading.Thread(target=self.گوش_دادن, daemon=True).start()

    def تنظیم_زنجیره(self, زنجیره):
        self.زنجیره = زنجیره

    def گوش_دادن(self):
        print(f"نود روی پورت {self.پورت} آماده دریافت پیام است.")
        while True:
            ارتباط, آدرس = self.سرور.accept()
            threading.Thread(target=self.دریافت_پیام, args=(ارتباط,), daemon=True).start()

    def دریافت_پیام(self, ارتباط):
        try:
            داده = ارتباط.recv(4096).decode(کدگذاری)
            پیام = json.loads(داده)
            نوع = پیام.get('نوع')
            if نوع == 'بلاک':
                بلاک = پیام['داده']
                print("دریافت بلاک جدید:", بلاک)
                # اینجا می‌توانید بلاک را به زنجیره اضافه کنید
            elif نوع == 'تراکنش':
                تراکنش = پیام['داده']
                print("دریافت تراکنش جدید:", تراکنش)
                # اینجا می‌توانید تراکنش را به استخر اضافه کنید
            elif نوع == 'درخواست_زنجیره':
                if self.زنجیره:
                    self.ارسال_پیام(ارتباط, 'زنجیره', self.زنجیره)
            elif نوع == 'زنجیره':
                print("دریافت زنجیره:", پیام['داده'])
            else:
                print("پیام ناشناخته:", پیام)
        except Exception as e:
            print("خطا در دریافت پیام:", e)
        finally:
            ارتباط.close()

    def ارسال_پیام(self, مقصد, نوع, داده):
        پیام = json.dumps({'نوع': نوع, 'داده': داده})
        if isinstance(مقصد, tuple):
            # ارسال به نود دیگر
            try:
                ارتباط = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ارتباط.connect(مقصد)
                ارتباط.sendall(پیام.encode(کدگذاری))
                ارتباط.close()
            except Exception as e:
                print(f"خطا در ارسال پیام به {مقصد}: {e}")
        else:
            # ارسال به کلاینت متصل
            try:
                مقصد.sendall(پیام.encode(کدگذاری))
            except Exception as e:
                print("خطا در ارسال پیام به کلاینت:", e)

    def پخش_به_همسایه_ها(self, نوع, داده):
        for همسایه in self.نودهای_همسایه:
            self.ارسال_پیام(همسایه, نوع, داده)

    def درخواست_زنجیره_از_همسایه(self):
        for همسایه in self.نودهای_همسایه:
            self.ارسال_پیام(همسایه, 'درخواست_زنجیره', None)

# نمونه استفاده
if __name__ == "__main__":
    نود۱ = نود(پورت=5000, نودهای_همسایه=[('127.0.0.1', 5001)])
    نود۲ = نود(پورت=5001, نودهای_همسایه=[('127.0.0.1', 5000)])
    import time
    time.sleep(1)
    نود۱.ارسال_پیام(('127.0.0.1', 5001), 'تراکنش', {'فرستنده': 'A', 'گیرنده': 'B', 'مقدار': 5})
    نود۲.درخواست_زنجیره_از_همسایه() 