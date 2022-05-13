from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class Trade_Type(str, Enum):
    BUY = 'BUY'
    SELL = 'SELL'

class StockTrade(BaseModel):
    account_no: str
    symbol: str
    quantity: int
    price: float
    trade_date: str
    trade_type: Trade_Type

    class Config:
        use_enum_values = True

class MutualFundTrade(BaseModel):
    account_no: str
    symbol: str
    quantity: int
    price: float
    trade_date: str
    trade_type: Trade_Type

    class Config:
        use_enum_values = True

class BullionTrade(BaseModel):
    account_no: str
    symbol: str
    quantity: int
    price: float
    trade_date: str
    trade_type: Trade_Type

    class Config:
        use_enum_values = True