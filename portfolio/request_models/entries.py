from numpy import quantile
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class Trade_Type(str, Enum):
    BUY = 'BUY'
    SELL = 'SELL'

class IPFrequency(str, Enum):
    Monthly = 'Monthly'
    Quarterly = 'Quarterly'
    HalfYearly = 'Half-Yearly'
    Yearly = 'Yearly'
    Maturity = 'Maturity'



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
    quantity: float
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

class ListedNCDTrade(BaseModel):
    account_no:str
    name:str
    trade_date:str
    trade_type:Trade_Type
    quantity:int
    price:float

    class Config:
        use_enum_values=True


class UnlistedBondTrade(BaseModel):
    account_no: str
    name: str
    interest_rate: float
    quantity: int
    price: float
    bond_yield: float
    buy_price: float
    buy_date: str
    maturity_date: str
    maturity_amount: float
    ip_frequency: IPFrequency


class FDTrade(BaseModel):
    account_no: str
    total_amount: float
    interest_rate: float
    start_date: str
    maturity_date: str
    maturity_amount: float
    ip_frequency: IPFrequency

    class Config:
        use_enum_values = True