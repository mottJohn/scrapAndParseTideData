year = '2019'
fileName = 'Tide_2019.csv'

import requests
import pandas as pd
from datetime import timedelta, date
import datetime

df = pd.read_csv("data.txt", sep='\s+', header=None, skiprows=[0], dtype=str) #read the text file
df_1 = df.iloc[:,0:4] #slice cols
df_2 = df.iloc[:,[0,1,4,5]]
df_3 = df.iloc[:,[0,1,6,7]]
df_4 = df.iloc[:,[0,1,8,9]]

cols = ['mm', 'dd', 'Time', 'Tide Height(m)'] #set col name
df_1.columns = cols
df_2.columns = cols
df_3.columns = cols
df_4.columns = cols

data = pd.concat([df_1, df_2, df_3, df_4]) # concat alone rows
data['yyyy'] = year #set year
data['DateTime'] = data['dd'] + data['mm'] + data['yyyy'] + data['Time'] #get datetime
data = data.drop(columns = ['dd','mm','yyyy']) #drop the useless columns
data['DateTime'] = pd.to_datetime(data['DateTime'], format='%d%m%Y%H%M') #convert to datetime format
data = data.sort_values('DateTime') #sort
data = data.dropna() #drop nan
data['Date'] =  data['DateTime'].dt.normalize() #get date only
data['Time'] = data['DateTime'].dt.time #get time only
data = data.drop(columns = ['DateTime']) #drop the uselss col
data['Date'] = data['Date'].dt.strftime('%d/%m/%Y') #format date
data = data[['Date','Time','Tide Height(m)']] #rearange columns

data.to_csv(fileName, index = False) #save to csv
print(data)

"""
#check NAN
print(data.isna().sum())
print(df_1.isna().sum() + df_2.isna().sum() + df_3.isna().sum() + df_4.isna().sum())
"""