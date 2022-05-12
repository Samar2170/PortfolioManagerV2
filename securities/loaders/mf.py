import pandas as pd
import os
from securities.models.mf import MutualFund

def load_mutual_funds():
    """
    Loads the mutual funds data from the CSV file.
    """
    path = os.path.join("Init_Assets/Securities/", "AllMFs.csv")
    mf_df = pd.read_csv(path)
    objs = []
    for index, row in mf_df.iterrows():
        mf = MutualFund(
            name=row['Name'],
            sub_category=row['Sub Category'],
            plan=row['Plan'],
            expense_ratio=row['Expense Ratio'],
            aum=row['AUM'],
        )
        objs.append(mf)
    MutualFund.objects.bulk_create(objs)
    print("Mutual Funds loaded successfully.")
    return
    