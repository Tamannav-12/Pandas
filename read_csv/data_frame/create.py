import numpy as np 
import pandas as pd
student =[[10,20,2],
          [13,12,3],
          [24,34,8],
          [33,43,9]]

student_set = pd.DataFrame(student,columns=['iq','marks','package'])
print(student_set)
