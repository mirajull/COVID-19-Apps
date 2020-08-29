import csv
import pandas as pd

df=pd.read_csv("trackers.csv")

cols=[]

for i in df:
    cols.append(i)

for index, row in df.iterrows():
    for i in range(len(cols)):
        print(row[cols[i]], end='')
        if i!=len(cols)-1:
            print(' & ', end='')
    print("\\\ \hline")
