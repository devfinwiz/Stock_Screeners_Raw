'''Run this script after execution of CSVGenerator is completed. The sole objective of this script is to filter the tickers whose data is insufficient on YFinance.'''
'''Removes tickers that are delisted from the exchange and updates Tickers.csv'''

from os import listdir
import csv
import os
import pandas as pd

def conLiToLiOfLi(lst):
    return [[el] for el in lst]

def find_csv(path_to_dir,suffix=".NS.csv"):
    filenames=listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]

curdir=os.getcwd()
fn=find_csv(curdir)
hold=[]
hold3=[]
for name in fn:
    with open(name,'r') as csvfile:
        csv_dict=[row for row in csv.DictReader(csvfile)]
        if(len(csv_dict)<2):
            hold.append(name)
print(hold)

with open("Auto generated Dataset\Tickers.csv",'r',newline='') as f:
    reader=csv.reader(f)
    data=list(reader)
    #print(data)
    hold3=data

for i in range(0,len(hold3)):
    hold3[i]=hold3[i][0]

#print(hold3)
print(len(hold))
print(len(hold3))

for i in range(0,len(hold)):
    hold[i]=hold[i].strip('.csv')

for i in range(0,len(hold)):
    if(hold[i] in hold3):
        hold3.remove(hold[i])

print(len(hold3))
#print(hold3)

lstoflst=conLiToLiOfLi(hold3)
#print(lstoflst)

#for check in hold:
    #os.remove(check)

with open("Auto generated Dataset\Tickers.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(lstoflst)
    
        
                



    
