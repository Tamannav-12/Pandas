import pandas as pd
vk=pd.read_csv(r"C:\Users\Lenovo\Downloads\kohli_ipl.csv" , index_col='match_no')
series=vk.squeeze()
print(series.sample())


print(type(series))