import pandas as pd
import os
from securities.models.debt import ListedNCD


def load_listed_ncd():
    path=os.path.join("Init_Assets/Securities/", "BondsIndexx.xlsx")
    df = pd.read_excel(path)
    for _, row in df.iterrows():
        ncd = ListedNCD(
            name=row['Name'],
            symbol1=row['Name'],
            face_value=row['FV'],
            maturity_date=row['Maturity'],
            maturity_amount=row['RV'],
            interest_rate=row['Coupon'],
            ip_frequency=row['Freq'],
            ip_amount=row['Coupon']*row['FV'],
            is_interest_rate_floating=False,
            isin_code=row['isin'],
            dirty_price=row['Price'],

        )
        ncd.save()
    print("Listed NCDs loaded successfully.")