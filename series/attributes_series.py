import pandas as pd
marks={ 'english':
       33,'hindi':45,'maths':22}
marks_series=pd.Series(marks,name='Tamanna ke marks')

print(marks_series.size)
print(marks_series.index)
print(marks_series.dtype)
print(marks_series.is_unique)
print(marks_series.name)
