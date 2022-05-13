from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class Trade_Type(str, Enum):
    BUY = 'BUY'
    SELL = 'SELL'

class StockTrade(BaseModel):
    symbol: str
    quantity: int
    price: float
    date: str
    trade_type: Trade_Type

    class Config:
        use_enum_values = True

