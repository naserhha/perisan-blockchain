# API تراکنش‌ها برای PersianChain (FastAPI)
from fastapi import APIRouter, Body

router = APIRouter()

# داده نمونه تراکنش‌ها
تراکنش_ها = [
    {"فرستنده": "A", "گیرنده": "B", "مقدار": 10},
    {"فرستنده": "B", "گیرنده": "C", "مقدار": 5}
]

@router.get("/transactions")
def get_transactions():
    return تراکنش_ها

@router.post("/transactions")
def add_transaction(تراکنش: dict = Body(...)):
    تراکنش_ها.append(تراکنش)
    return {"message": "تراکنش افزوده شد", "تراکنش": تراکنش} 