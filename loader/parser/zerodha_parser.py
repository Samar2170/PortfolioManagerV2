

def parse_zerodha_file(zdf):
    zdf.columns = zdf.iloc[21]
    drop_rows = [i for i in range(22)]
    zdf = zdf.drop(drop_rows)
    zdf.set_index('Symbol', inplace=True)
    zdf.drop(columns=['Unrealized P&L','Unrealized P&L Pct.','Quantity Pledged (Margin)','Quantity Pledged (Loan)'],axis=1,inplace=True)
    zdf['Invested']=zdf['Average Price']*zdf['Quantity Available']
    zdf['Current Value']=zdf['Previous Closing Price']*zdf['Quantity Available']

    equities_mask = (zdf['Sector']!='Debt') & (zdf['Sector']!='Others') 
    equities = zdf.loc[equities_mask]

    debt_mask = (zdf['Sector']=='Debt')
    debt = zdf.loc[debt_mask]

    others_mask = (zdf['Sector']=='Others')
    others = zdf.loc[others_mask]

    return equities, debt, others

def parse_zerodha_mf_file(zdf):
    zdf.columns = zdf.iloc[21]
    drop_rows = [i for i in range(22)]
    zdf = zdf.drop(drop_rows)
    zdf.set_index('Symbol', inplace=True)
    zdf['Instrument Type'].fillna('Others',inplace=True)
    zdf.fillna(0,inplace=True)
    zdf.drop(columns=['Unrealized P&L','Unrealized P&L Pct.','Quantity Pledged (Margin)','Quantity Pledged (Loan)'],axis=1,inplace=True)
    zdf['Invested']=zdf['Average Price']*zdf['Quantity Available']
    zdf['Current Value']=zdf['Previous Closing Price']*zdf['Quantity Available']

    return zdf 
    