import pandas as pd
import os
from securities.models.stocks import Stock

CONTEXT_DIR = "Init_Assets/Securities/"

def load_stocks():
    """
    Loads the stocks data from the CSV file.
    """
    path = os.path.join(CONTEXT_DIR, "ind_nifty500list.csv")
    stocks_df = pd.read_csv(path)
    
    objs = []
    for index, row in stocks_df.iterrows():
        stock = Stock(
            company_name=row['Company Name'],
            symbol=row['Symbol'],
            industry=row['Industry'],
            isin_code = row['ISIN Code'],
        )
        objs.append(stock)
    Stock.objects.bulk_create(objs)
    print("Stocks loaded successfully.")
    return

