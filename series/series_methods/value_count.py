import pandas as pd
vk=pd.read_csv(r"C:\Users\Lenovo\Downloads\kohli_ipl.csv" , index_col='match_no')
series=vk.squeeze()
movies=pd.read_csv(r"C:\Users\Lenovo\Downloads\bollywood.csv" , index_col='movie')
series2=movies.squeeze()

print(series2.value_counts())
print(series.sort_values())
print(series.sort_index())

#inplace parameter hota hai jisse parmanent change kar skate hai series ko 