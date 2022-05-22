from securities.models.mf import MutualFund
from securities.models.bullion import Bullion
from securities.models.stocks import Stock
from securities.models.debt import ListedNCD
from securities.views import BaseSearchSecurities, BaseSecurity, BaseSecurities


class SearchMutualFunds(BaseSearchSecurities):
    Securities_Model=MutualFund

class SearchStocks(BaseSearchSecurities):
    Securities_Model=Stock

class StockView(BaseSecurity):
    Securities_Model=Stock

class MutualFundView(BaseSecurity):
    Securities_Model=MutualFund

class ListNCDView(BaseSecurity):
    Securities_Model=ListedNCD

class StockList(BaseSecurities):
    Securities_Model=Stock

class MutualFundList(BaseSecurities):
    Securities_Model=MutualFund

class ListNCDList(BaseSecurities):
    Securities_Model=ListedNCD

class BullionList(BaseSecurities):
    Securities_Model=Bullion


