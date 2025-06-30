# PersianChain Web API - FastAPI
# نویسنده: Mohammad Nasser Haji Hashemabad
# توضیحات: نقطه شروع API برای PersianChain

from fastapi import FastAPI
from api import blockchain, transactions, accounts, mempool, fee, security

app = FastAPI(
    title="PersianChain Web API",
    description="API برای مدیریت و مشاهده بلاکچین فارسی PersianChain",
    version="1.0.0"
)

app.include_router(blockchain.router, prefix="/blockchain")
app.include_router(transactions.router, prefix="/blockchain")
app.include_router(accounts.router, prefix="/blockchain")
app.include_router(mempool.router, prefix="/blockchain")
app.include_router(fee.router, prefix="/blockchain")
app.include_router(security.router, prefix="/blockchain")

@app.get("/")
def home():
    return {"message": "PersianChain Web API فعال است"} 