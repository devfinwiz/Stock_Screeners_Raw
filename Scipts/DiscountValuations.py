'''Filter stocks trading at a discount based on their book value parameter and also that are trading lower than their fair value based on their annual sales.'''

import csv
import traceback
from itertools import zip_longest
from sympy import Q
from yahoofinancials import YahooFinancials
from more_itertools import unique_everseen

tickers_name=[]
tickers_close=[]
tickers_percent=[]
tickers_vabv=[]
tickers_vas=[]

def discount_as_per_bv():
    with open(r"Auto generated Dataset\Valuations.csv",'r') as mf:
        data=csv.DictReader(mf)

        for row in data:
            try:
                vabv=float(row['Valuation As Per Book Value'])
                ltp=float(row['LTP'])
                if(ltp<vabv):
                    
                    percent=((vabv-ltp)/vabv)*100
                    percent=round(percent,2)
                    tickers_name.append(row['Ticker'])
                    tickers_vabv.append(round(float(row['Valuation As Per Book Value']),2))
                    tickers_close.append(row['LTP'])
                    tickers_percent.append(percent)
                

            except Exception as e:
                print(row['Ticker'])
                print(traceback.format_exc())

    store(tickers_name,tickers_vabv,tickers_close,tickers_percent,"Discount_BookValue","Valuation-Book Value")

def store(l1,l2,l3,l4,filename,aim): #aim: Valuation-Book Value or Valuation - Sales
    list_clubber=[l1,l2,l3,l4]
    export_data_complete=zip_longest(*list_clubber,fillvalue='')

    with open(r"Auto generated Dataset\{}.csv".format(filename),'w',encoding="ISO-8859-1",newline="") as myfile:
        wr=csv.writer(myfile)
        wr.writerow(("Ticker",aim,"LTP","Discount(%)"))
        wr.writerows(export_data_complete)
        print("Execution Success!")
    
    tickers_name.clear()
    tickers_close.clear()
    tickers_percent.clear()

discount_as_per_bv()


def discount_as_per_sales():
    with open(r"Auto generated Dataset\Valuations.csv",'r') as mf:
        data=csv.DictReader(mf)

        for row in data:
            try:
                vas=float(row['Valuation As Per Sales'])
                ltp=float(row['LTP'])

                if(ltp<vas):
                    
                    percent=((vas-ltp)/vas)*100
                    percent=round(percent,2)
                    tickers_name.append(row['Ticker'])
                    tickers_vas.append(round(float(row['Valuation As Per Sales']),2))
                    tickers_close.append(row['LTP'])
                    tickers_percent.append(percent)
                

            except Exception as e:
                print(row['Ticker'])
                print(traceback.format_exc())

    store(tickers_name,tickers_vas,tickers_close,tickers_percent,"Discount_Sales","Valuation-Sales")

discount_as_per_sales()
print("Execution Success!")