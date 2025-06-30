# API بلاکچین برای PersianChain (FastAPI)
from fastapi import APIRouter

router = APIRouter()

# داده نمونه بلاک‌ها
بلاک_ها = [
    {"شماره": 0, "تراکنش_ها": [], "هش": "000..."},
    {"شماره": 1, "تراکنش_ها": [{"فرستنده": "A", "گیرنده": "B", "مقدار": 10}], "هش": "abc..."}
]

@router.get("/blocks")
def get_blocks():
    return بلاک_ها 