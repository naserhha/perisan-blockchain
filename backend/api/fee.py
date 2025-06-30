# API کارمزد تراکنش‌ها برای PersianChain (FastAPI)
from fastapi import APIRouter, Body

router = APIRouter()

# داده نمونه کارمزدها (در عمل باید از تراکنش‌های استخر محاسبه شود)
کارمزد_ها = [2, 1, 3]

@router.get("/fee")
def get_total_fee():
    return {"total_fee": sum(کارمزد_ها)}

@router.post("/fee")
def add_fee(داده: dict = Body(...)):
    مقدار = داده.get("مقدار", 0)
    کارمزد_ها.append(مقدار)
    return {"message": "کارمزد افزوده شد", "مقدار": مقدار, "total_fee": sum(کارمزد_ها)} 