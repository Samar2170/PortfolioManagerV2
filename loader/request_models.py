from pydantic import BaseModel
from typing import Optional
from enum import Enum

class IpFrequency(str, Enum):
    Monthly = 'monthly'
    Quarterly = 'quarterly'
    Weekly = 'weekly'
    Yearly = 'yearly'
    Maturity = 'maturity'


class LoaderHoldingRequest(BaseModel):
    account_no: str

class StockHoldingEntry(BaseModel):
    symbol: str
    quantity: int
    buy_price: float

class BondHoldingEntry(BaseModel):
    symbol: str
    account_no: str
    quantity: int
    buy_price: float
    total_amount: float
    buy_date: str
    bond_yield: float

class FDHoldingEntry(BaseModel):
    account_no: str
    total_amount: float
    interest_rate: float
    ip_frequency: str
    start_date: str
    maturity_date: str
    maturity_amount: float
    isin_code: Optional[str]
