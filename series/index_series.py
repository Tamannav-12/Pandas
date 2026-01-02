import pandas as pd
marks=[11,12,15]
subjects=['maths','english','hindi']
print(pd.Series(marks,index=subjects))
#give the name of this file
print(pd.Series(marks,index=subjects,name='Tamanna ke marks')) 
