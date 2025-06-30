# API حساب‌ها برای PersianChain (FastAPI)
from fastapi import APIRouter, Body

router = APIRouter()

# داده نمونه حساب‌ها
حساب_ها = {
    "A": 90,
    "B": 55,
    "C": 5
}

@router.get("/accounts")
def get_accounts():
    return حساب_ها

@router.post("/accounts")
def add_account(داده: dict = Body(...)):
    آدرس = داده.get("آدرس")
    مقدار = داده.get("مقدار", 0)
    if آدرس in حساب_ها:
        return {"message": "این حساب قبلاً وجود دارد."}
    حساب_ها[آدرس] = مقدار
    return {"message": "حساب افزوده شد", "آدرس": آدرس, "مقدار": مقدار} 