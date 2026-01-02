import pandas as pd
file=pd.read_csv(r"C:\Users\Lenovo\Downloads\subs.csv")
series=file.squeeze()
print(type(series))
print(series)