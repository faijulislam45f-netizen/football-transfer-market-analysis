import pandas as pd
import os

files = [f for f in os.listdir('.') if f.endswith('transfers_history.csv')]

print(f"{'File Name':<25} | {'Rows':<6} | {'Cols':<5} | {'Columns'}")
print("-" * 80)

for file in files:
    try:
        df = pd.read_csv('transfers_history.csv')
        # Columns ki list ko string mein convert kiya
        cols_list = ", ".join(df.columns.tolist())
        print(f"{file:<25} | {df.shape[0]:<6} | {df.shape[1]:<5} | {cols_list}")
    except Exception as e:
        print(f"{file:<25} | Error")


