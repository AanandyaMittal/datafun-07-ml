import pandas as pd
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')
nyc.columns = ['Date','Temperature','Anomaly']
nyc.Date - nyc.Date.floordiv(100)
nyc.head(3)