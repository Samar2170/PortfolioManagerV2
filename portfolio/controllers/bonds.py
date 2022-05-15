from portfolio.models.accounts import fetch_account
from util.exceptions import ValidationException
from datetime import datetime
from portfolio.models.accounts import DematAccount
from portfolio.models.debt import ListedNCD, ListedNCDBuyTrade, ListedNCDHolding, ListedNCDSellTrade

class BaseBondController:
    Security_Model =None
    Holding_Model = None
    Buy_Trade_Model = None
    Sell_Trade_Model = None

    def __init__(self, name,account_code):
        self.account = fetch_account(account_code)
        try:
            self.security = self.Security_Model.objects.get(name=name)
        except self.Security_Model.DoesNotExist:
            raise ValidationException('Security not found')
    
    def record_trade(self, trade):
        check_holding=self.check_holding()
        check_holding_today=self.check_holding(for_today=True)
        if check_holding_today and trade.trade_type == 'BUY':
            if self.Buy_Trade_Model is not None:
                self.Buy_Trade_Model.objects.create(account=self.account,security=self.security,quantity=trade.quantity,
                                                    price=trade.price,total_amount=trade.quantity * trade.price,trade_date=trade.trade_date,trade_id=trade.trade_id)
            holding=self.Holding_Model.objects.get(security=self.security, account=self.account,buy_date=datetime.now().date())
            holding.quantity += trade.quantity
            holding.total_amount += trade.quantity * trade.price
            holding.buy_price = holding.total_amount / holding.quantity
            holding.save(update_fields=['quantity','total_amount', 'buy_price'])
        if not check_holding_today and trade.trade_type == 'BUY':
            if self.Buy_Trade_Model is not None:
                self.Buy_Trade_Model.objects.create(account=self.account,security=self.security,quantity=trade.quantity,
                                                    price=trade.price,total_amount=trade.quantity * trade.price,trade_date=trade.trade_date,trade_id=trade.trade_id)

            holding=self.Holding_Model.objects.create(security=self.security,account=self.account,
                                                    quantity=trade.quantity,buy_price=trade.price,
                                                    total_amount = trade.quantity * trade.price,
                                                    buy_date=datetime.now().date())
        if check_holding and trade.trade_type == 'SELL':
            if self.Sell_Trade_Model is not None:
                self.Sell_Trade_Model.objects.create(account=self.account,security=self.security,quantity=trade.quantity,
                                                    price=trade.price,total_amount=trade.quantity * trade.price,trade_date=trade.trade_date,trade_id=trade.trade_id)
            holding=self.Holding_Model.objects.get(security=self.security, account=self.account)
            holding.quantity -= trade.quantity
            holding.total_amount -= trade.quantity * holding.buy_price
            holding.save(update_fields=['quantity','total_amount'])
        if not check_holding and trade.trade_type == 'SELL':
            raise ValidationException('No holding found')


    def check_holding(self,for_today=False ):
        try:
            if for_today==True:
                holding = self.Holding_Model.objects.get(security=self.security, account=self.account, 
                                                    buy_date=datetime.now().date())
                return True
            else:
                holding = self.Holding_Model.objects.get(security=self.security, account=self.account)
                return True
        except self.Holding_Model.DoesNotExist:
            return False

class ListedNCDController(BaseBondController):
    Security_Model = ListedNCD
    Holding_Model = ListedNCDHolding
    Buy_Trade_Model = ListedNCDBuyTrade
    Sell_Trade_Model = ListedNCDSellTrade
