import pandas as pd
from celery import shared_task
from loader.models import File, StockHoldingFile, ListedNCDHoldingFile, FDHoldingFile,MFHoldingFile
from loader.request_models import FDHoldingEntry, StockHoldingEntry, BondHoldingEntry
from securities.models.debt import ListedNCD
from securities.models.stocks import Stock
from securities.models.mf import MutualFund

from portfolio.models.stocks import StockHolding
from portfolio.models.mf import MutualFundHolding
from portfolio.models.fd import FixedDepositHolding
from portfolio.models.debt import ListedNCDHolding


# @shared_task
def parse_ot_stock_holding(file_id):
    # import ipdb; ipdb.set_trace()
    all_symbols = set(Stock.objects.all().values_list('symbol', flat=True))
    file_obj=StockHoldingFile.objects.get(id=file_id)
    if file_obj.format == 'csv':
        df = pd.read_csv(file_obj.file_path)
    elif file_obj.format == 'xlsx':
        df = pd.read_excel(file_obj.file_path)
    else:
        return "Invalid file format"
    
    
    cols=list(df.columns)
    if not StockHoldingFile.validate_columns(cols):
        file_obj.parse_response="Invalid columns"
        file_obj.save()
        return False
    
    if not StockHoldingFile.validate_format(file_obj.format):
        file_obj.parse_response="Invalid format"
        file_obj.save()
        return False
    
    df['symbol']=df['symbol'].str.upper()
    df['symbol']=df['symbol'].str.replace('-X',"")
    df['symbol']=df['symbol'].str.replace('-Z',"")
    symbols = [s for s in df['symbol'] if s in all_symbols] 


    df=df.to_dict('records')
    


    for key in df:
        input_dict = StockHoldingEntry(**key)
        if input_dict.symbol in symbols:
            stock=Stock.objects.get(symbol=input_dict.symbol)
            if not stock:
                file_obj.parse_response="Invalid symbol"
                file_obj.save()
                return False

            holding =StockHolding.objects.get_or_create(
                account=file_obj.account,
                security=stock,
                quantity=input_dict.quantity,
                buy_price=input_dict.buy_price,
                total_amount=input_dict.quantity*input_dict.buy_price
            )     

    file_obj.parse_response="Success"
    file_obj.save()
    return True


# @shared_task
# def parse_ot_mf_holding(file_id):
#     # import ipdb; ipdb.set_trace()
#     file_obj=MFHoldingFile.objects.get(id=file_id)
#     if file_obj.format == 'csv':
#         df = pd.read_csv(file_obj.file_path)
#     elif file_obj.format == 'xlsx':
#         df = pd.read_excel(file_obj.file_path)
#     else:
#         return "Invalid file format"
    
    
#     cols=list(df.columns)
#     if not MFHoldingFile.validate_columns(cols):
#         file_obj.parse_response="Invalid columns"
#         file_obj.save()
#         return False
    
#     if not MFHoldingFile.validate_format(file_obj.format):
#         file_obj.parse_response="Invalid format"
#         file_obj.save()
#         return False
    
#     df['symbol']=df['symbol'].apply(lambda x: x.split('-')[0])
#     df=df.to_dict('records')
#     for key in df:
#         input_dict = StockHoldingEntry(**key)
#         mf=MutualFund.objects.get(name=input_dict.symbol)
#         if not mf:
#             file_obj.parse_response="Invalid symbol"
#             file_obj.save()
#             return False

#         holding =MutualFundHolding.objects.get_or_create(
#             account=file_obj.account,
#             security=mf,
#             quantity=input_dict.quantity,
#             buy_price=input_dict.buy_price,
#             total_amount=input_dict.quantity*input_dict.buy_price,
#         )     
#     file_obj.parse_response="Success"
#     file_obj.save()
#     return True


@shared_task
def parse_ot_fd_holding(file_id):
    file_obj=FDHoldingFile.objects.get(id=file_id)
    if file_obj.format == 'csv':
        df = pd.read_csv(file_obj.file_path)
    elif file_obj.format == 'xlsx':
        df = pd.read_excel(file_obj.file_path)
    else:
        return "Invalid file format"
    
    
    cols=list(df.columns)
    if not FDHoldingFile.validate_columns(cols):
        file_obj.parse_response="Invalid columns"
        file_obj.save()
        return False
    
    if not FDHoldingFile.validate_format(file_obj.format):
        file_obj.parse_response="Invalid format"
        file_obj.save()
        return False
    
    df=df.to_dict('records')
    for k,v in df.items():
        input_dict = FDHoldingEntry(**v)
        holding =FixedDepositHolding.objects.get_or_create(
            account=file_obj.account,
            total_amount=input_dict.total_amount,
            interest_rate=input_dict.interest_rate,
            ip_frequency=input_dict.ip_frequency,
            start_date=input_dict.start_date,
            maturity_date=input_dict.maturity_date,
            maturity_amount=input_dict.maturity_amount,
            isin_code=input_dict.isin_code
        )     
    file_obj.parse_response="Success"
    file_obj.save()
    return True


# @shared_task
# def parse_ot_bond_holding(file_id):
#     file_obj=ListedNCDHoldingFile.objects.get(id=file_id)
#     if file_obj.format == 'csv':
#         df = pd.read_csv(file_obj.file_path)
#     elif file_obj.format == 'xlsx':
#         df = pd.read_excel(file_obj.file_path)
#     else:
#         return "Invalid file format"
    
    
#     cols=list(df.columns)
#     if not ListedNCDHoldingFile.validate_columns(cols):
#         file_obj.parse_response="Invalid columns"
#         file_obj.save()
#         return False
    
#     if not ListedNCDHoldingFile.validate_format(file_obj.format):
#         file_obj.parse_response="Invalid format"
#         file_obj.save()
#         return False
    
#     df=df.to_dict('records')
#     for k,v in df.items():
#         input_dict = BondHoldingEntry(**v)
#         bond=ListedNCD.objects.get(isin_code=input_dict.isin_code)
#         if not bond:
#             file_obj.parse_response="Invalid symbol"
#             file_obj.save()
#             return False

#         holding =ListedNCDHolding.objects.get_or_create(
#             account=file_obj.account,
#             security=bond,
#             quantity=input_dict.quantity,
#             buy_price=input_dict.buy_price,
#             total_amount=input_dict.total_amount,
#         )     
#     file_obj.parse_response="Success"
#     file_obj.save()
#     return True