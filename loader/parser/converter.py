from loader.parser.zerodha_parser import parse_zerodha_file, parse_zerodha_mf_file
from loader.models import StockHoldingFile
from loader.request_models import StockHoldingEntry
import pandas as pd
from securities.models.stocks import Stock
from portfolio.models.stocks import StockHolding


def zdf_to_input_dict(file_id):
    file_obj=StockHoldingFile.objects.get(id=file_id)
    if file_obj.format == 'csv':
        df = pd.read_csv(file_obj.file_path)
    elif file_obj.format == 'xlsx':
        df = pd.read_excel(file_obj.file_path)
    else:
        return "Invalid file format"
    
    equities, _, _ = parse_zerodha_file(df)
    equities.reset_index(inplace=True)
    equities.rename(columns={"Symbol":"symbol","Quantity Available":"quantity","Average Price":"buy_price"},inplace=True)
    drop_cols = [x for x in equities.columns if isinstance(x,str) and  not x.islower()]
    equities.drop(drop_cols, axis=1, inplace=True)
    equities.dropna(axis=1,inplace=True)
    equities['quantity'] = equities['quantity'].astype(int)
    equities["total_amount"] = equities["quantity"] * equities["buy_price"]
    
    equities["symbol"]=equities["symbol"].apply(lambda x: x.split('-')[0])
    equities["symbol"]=equities["symbol"].str.upper()
    df=equities
    all_symbols = set(Stock.objects.all().values_list('symbol', flat=True))
    symbols = [s for s in df['symbol'] if s in all_symbols]
    df=df.to_dict('records')
    

    resp=[]
    for key in df:
        input_dict = StockHoldingEntry(**key)
        if input_dict.symbol in symbols:
            stock=Stock.objects.get(symbol=input_dict.symbol)
            if not stock:
                resp.append("({},{})".format(input_dict.symbol,"Invalid symbol"))

            holding =StockHolding.objects.get_or_create(
                account=file_obj.account,
                security=stock,
                quantity=input_dict.quantity,
                buy_price=input_dict.buy_price,
                total_amount=input_dict.quantity*input_dict.buy_price
            )
            resp.append("({},{})".format(input_dict.symbol,"Success"))     

    if len(resp)==0:
        resp.append("No data to save")
    file_obj.parse_response="\n".join(resp)
    file_obj.save()
    return True