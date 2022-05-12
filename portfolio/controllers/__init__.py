from gc import get_threshold
from portfolio.models.accounts import fetch_account

class BaseController:
    Security_Model =None
    Sell_Trade_Model = None
    Buy_Trade_Model = None
    Holding_Model = None
    
    def __init__(self, symbol,account_code):
        self.account = fetch_account(account_code)
        self.security = self.Security_Model.objects.get(symbol=symbol)

    def record_trade(self, trade):
        if trade.trade_type == 'BUY':
            self.Buy_Trade_Model.objects.create(
                account=self.account,
                security=self.security,
                quantity=trade.quantity,
                price=trade.price,
                total_amount=trade.quantity * trade.price,
                trade_date=trade.trade_date,
            )
        elif trade.trade_type == 'SELL':
            holding = self.Holding_Model.objects.get(
                security=self.security,
                account=self.account,
            )
            self.Sell_Trade_Model.objects.create(
                account=self.account,
                security=self.security,
                quantity=trade.quantity,
                buy_price=holding.buy_price,
                sell_price=trade.price,
                total_amount=trade.quantity * trade.price,
                trade_date=trade.trade_date,
            )
        else:
            raise Exception('Invalid trade type')
        self.handle_trade(trade)

    
    def handle_trade(self, trade):
        check_holding = self.check_holding()
        if check_holding and trade.trade_type == 'BUY':
            holding = self.Holding_Model.objects.get(security=self.security, account=self.account)           
            holding.quantity += trade.quantity
            holding.total_amount += trade.quantity * trade.price
            holding.save(update_fields=['quantity','total_amount'])
            self.update_holding_price()
        
        elif check_holding and trade.trade_type == 'SELL':
            holding = self.Holding_Model.objects.get(security=self.security, account=self.account)           
            holding.quantity -= trade.quantity
            holding.total_amount -= trade.quantity * holding.buy_price
            holding.save(update_fields=['quantity','total_amount'])
            self.update_holding_price()

        elif not check_holding and trade.trade_type == 'BUY':
            holding = self.Holding_Model.objects.create(
                security=self.security,
                account=self.account,
                quantity=trade.quantity,
                buy_price=trade.price,
                total_amount = trade.quantity * trade.price,
            )
        elif not check_holding and trade.trade_type == 'SELL':
            raise Exception('No holding found')
        else:
            raise Exception('Invalid trade type')
        
    def update_holding_price(self):
        holding = self.Holding_Model.objects.get(
            security=self.security,
            account=self.account,
        )
        holding.buy_price = holding.total_amount / holding.quantity
        holding.save(update_fields=['buy_price'])
        return None

    def check_holding(self):
        try:
            holding = self.Holding_Model.objects.get(
                security=self.security,
                account=self.account,
            )
            return holding
        except self.Holding_Model.DoesNotExist:
            return None

