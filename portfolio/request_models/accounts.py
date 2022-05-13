from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class BankAccountRequest(BaseModel):
    account_no: str
    bank_name: str
    bank_code: str
    balance: float

    class Config:
        use_enum_values = True


class DematAccountRequest(BaseModel):
    account_no: str
    broker: str
    balance: float

    class Config:
        use_enum_values = True
