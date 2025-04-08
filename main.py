from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Mengizinkan akses dari frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti dengan domain frontend Anda saat produksi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Crypto AI Backend Active"}

@app.get("/price")
def get_price(symbol: str = Query("BTCUSDT")):
    try:
        res = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
        return res.json()
    except Exception as e:
        return {"error": str(e)}

@app.post("/order")
def place_order(symbol: str, side: str, quantity: float):
    return {
        "message": "This is a dummy order endpoint",
        "symbol": symbol,
        "side": side,
        "quantity": quantity
    }
