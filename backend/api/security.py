# API امنیت و رمزنگاری برای PersianChain (FastAPI)
from fastapi import APIRouter, Body
from security import رمزنگاری, مقابله_دوبار_خرج

router = APIRouter()

# نمونه رمزنگاری
رمز = رمزنگاری()
مقابله = مقابله_دوبار_خرج()

@router.post("/security/encrypt")
def encrypt_data(داده: dict = Body(...)):
    متن = داده.get("data", "")
    رمزنگاری_شده = رمز.رمزنگاری_داده(متن)
    return {"encrypted": رمزنگاری_شده, "key": رمز.دریافت_کلید()}

@router.post("/security/decrypt")
def decrypt_data(داده: dict = Body(...)):
    داده_رمز = داده.get("encrypted", "")
    try:
        رمزگشایی_شده = رمز.رمزگشایی_داده(داده_رمز)
        return {"decrypted": رمزگشایی_شده}
    except Exception as e:
        return {"error": str(e)}

@router.post("/security/double_spend")
def check_double_spend(داده: dict = Body(...)):
    نتیجه = مقابله.بررسی_تراکنش(داده)
    return {"is_unique": نتیجه} 