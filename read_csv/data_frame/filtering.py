import pandas as pd
import numpy as np
ipl =pd.read_csv(r"C:\Users\Lenovo\Downloads\ipl-matches.csv")
mask= ipl['MatchNumber']=='Final'
new_df=ipl[mask]
print(new_df[['Season','WinningTeam']])


