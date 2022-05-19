from pydantic import BaseModel




class StockHoldingRequest(BaseModel):
    account_no: str
    format: str

