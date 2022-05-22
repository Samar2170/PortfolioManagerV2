from re import L
from django.db import models
from portfolio.models.accounts import GeneralAccount,BankAccount,DematAccount
from django.contrib.auth.models import User

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='uploads/')
    file_name = models.CharField(max_length=100)
    format = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    parsed = models.BooleanField(default=False)
    parse_response=models.TextField(default="")
    

    VALID_COLS=[]
    VALID_FORMATS=['csv','xlsx']
    def __str__(self):
        return self.file_name
    
    @classmethod
    def validate_format(cls,format):
        return format in cls.VALID_FORMATS


    @classmethod
    def validate_columns(cls,cols):
        if type(cols)!=list:
            raise Exception("Cols should be passed as a list")

        count=0
        for c in cols:
            if c in cls.VALID_COLS:
                count+=1
            else:
                pass
        if len(cols)==count:
            return True
        else:
            return False    


class StockHoldingFile(File):
    account=models.ForeignKey(DematAccount, on_delete=models.CASCADE)
    VALID_COLS=['symbol','quantity','buy_price']

class ListedNCDHoldingFile(File):
    account = models.ForeignKey(DematAccount,on_delete=models.CASCADE)
    VALID_COLS=['symbol','account_no','quantity','buy_price','total_amount','buy_date','bond_yield']


class FDHoldingFile(File):
    account = models.ForeignKey(BankAccount,on_delete=models.CASCADE)

    VALID_COLS=['account_no', 'total_amount', 'interest_rate', 'ip_frequency', 'start_date', 'maturity_date', 'maturity_amount', 'isin_code']

class MFHoldingFile(File):
    account = models.ForeignKey(DematAccount,on_delete=models.CASCADE)
    VALID_COLS=[ 'symbol','quantity','buy_price']
    