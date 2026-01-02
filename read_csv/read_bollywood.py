import pandas as pd
vk=pd.read_csv(r"C:\Users\Lenovo\Downloads\bollywood.csv", index_col='movie')
series=vk.squeeze()
print(series)
print(type(series))