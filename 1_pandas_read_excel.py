from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import glob
%matplotlib inline
first = True

files = glob.glob("*.xls")
for x in files:
    print(x)
    #file = r'2018.01.xls'
    df = pd.read_excel(x, header=4)
    df = df.fillna(method='ffill')
    df = df[pd.to_numeric(df['동'], errors='coerce').notnull()]
    d = df[['난방요금']][df['호'].notnull() & (df['호'] != '호') & (df['호'] != '동계') & (df['호'] != '합계')]
    if first:
        print("init")
        data = pd.DataFrame()
        data['household'] = df['동'].map(str)+'-'+df['호'].map(str)
        first = False
    data[x[:7]] = d['난방요금']
    #data['size'] = 39
    #data.loc[data['household'].str.startswith('8-'), "size"] = 50
    #data.loc[data['household'].str.startswith('105-'), "size"] = 32
data.set_index('household')

data = data.sort_values(by=['2019.01'])
data.set_index('household')
data[data['household'].str.startswith('8-')]['2019.01'].plot()

data = data.transpose()
data.columns = data.iloc[0]
data = data[1:]    

for col in data:
    #print(col)
    for val in data[col]:
        #print(val)
        try:
            if val> 300000: 
                print("Household", col)
                print(data[col])
                data[col].plot(figsize=(16,10), legend=col)
                continue
        except TypeError:
            #print('type error', val)
            continue
