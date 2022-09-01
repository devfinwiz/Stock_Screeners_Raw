'''Determines exact valuation of a stock based upon its book value and its annual sales.'''

import csv
import traceback
from itertools import zip_longest
from yahoofinancials import YahooFinancials
from more_itertools import unique_everseen

tickers=[]
val_as_per_bv=[]
val_as_per_pts=[]
latest_close=[]

#-----------------------------------------------------------------------------------------
#Computes fair value for all tickers as per their book value and as per their annual sales

def valuation_computer():
    with open("Auto generated Dataset\FinancialsBunch.csv",'r') as mf:
        data=csv.DictReader(mf)

        for row in data:
            try:
                bv=float(row['Book Value'])
                pts=float(row['PToSales'])
                ltp=float(row['Close'])
                tickers.append(row['Ticker'])
                latest_close.append(row['Close'])

                if(pts>0):
                    fairvaluebv=1.5*bv
                    val_as_per_bv.append(fairvaluebv)
                else:
                    fairvaluebv=bv
                    val_as_per_bv.append(fairvaluebv)
                
                fairvaluepts=(float(row['Revenue'])/float(row['Shares Outstanding']))
                holder=((2-pts)/2)*100
                holder2=(float(row['Close'])*float(holder))/100
                fairvaluepts2=float(row['Close'])+holder2

                finalfairvaluepts=(fairvaluepts+fairvaluepts2)/2

                val_as_per_pts.append(finalfairvaluepts)
                
            
            except Exception as e:
                print(row['Ticker'])
                print(traceback.format_exc())

    list_clubber=[tickers,val_as_per_bv,val_as_per_pts,latest_close]
    export_data_complete=zip_longest(*list_clubber,fillvalue='')

    with open("Auto generated Dataset\Valuations.csv",'w',encoding="ISO-8859-1",newline="") as myfile:
        wr=csv.writer(myfile)
        wr.writerow(("Ticker","Valuation As Per Book Value","Valuation As Per Sales","LTP"))
        wr.writerows(export_data_complete)
        print("Execution Success!")