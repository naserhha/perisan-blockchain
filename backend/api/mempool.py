# API استخر تراکنش‌ها (Mempool) برای PersianChain (FastAPI)
from fastapi import APIRouter, Body

router = APIRouter()

# داده نمونه استخر تراکنش‌ها
استخر_تراکنش = [
    {"فرستنده": "X", "گیرنده": "Y", "مقدار": 3},
    {"فرستنده": "Y", "گیرنده": "Z", "مقدار": 7}
]

@router.get("/mempool")
def get_mempool():
    return استخر_تراکنش

@router.post("/mempool")
def add_to_mempool(تراکنش: dict = Body(...)):
    استخر_تراکنش.append(تراکنش)
    return {"message": "تراکنش به استخر افزوده شد", "تراکنش": تراکنش} 