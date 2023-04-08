'''Filters stocks trading at 10% discount to their book value. Discount amount filtering in % is flexible.'''

import csv
from itertools import zip_longest
#from yahoofinancials import YahooFinancials
from more_itertools import unique_everseen


'''tickers_undervalued=list()
t_under_book_value=list()
t_under_close_price=list()
tickers_same_as_book_value=list()

with open("Auto generated Dataset\Financials.csv",'r') as csvfile:
    data=csv.DictReader(csvfile)

    for row in data:
        if(float(row['Close'])<float(row['Book_Value'])):
            tickers_undervalued.append(row['Ticker'])
            t_under_book_value.append(row['Book_Value'])
            t_under_close_price.append(row['Close'])

            print(row['Ticker'])
            print("---------------")
            print("LTP: "+row['Close'])
            print("Book Value: "+row['Book_Value'])
            print("=========================================")
        elif(float(row['Close'])==float(row['Book_Value'])):
            tickers_same_as_book_value.append(row['Ticker'])
        else:
            pass

list_clubber_final=[tickers_undervalued,t_under_book_value,t_under_close_price]
export_data_complete=zip_longest(*list_clubber_final,fillvalue='')

with open("Auto generated Dataset\Filtered.csv",'w',encoding="ISO-8859-1",newline="") as myfile:
    wr=csv.writer(myfile)
    wr.writerow(("Ticker","Book Value","LTP"))
    wr.writerows(export_data_complete)'''

tickers_gre_50=[]
tickers_gre_50_close=[]
tickers_gre_50_bookval=[]

#-------------------------------------------------------------------------------------------------
#Filters stocks that are trading 10% discount to their book value as compared to Last Traded Price

def book_value_filter():
    with open(r"Auto generated Dataset\Financials.csv",'r') as mf:
        data=csv.DictReader(mf)

        for row in data:
            
            hold=((float(row['Book Value'])-float(row['Close']))/float(row['Book Value'])*100)
            hold=round(hold,2)
            
            if(hold>10):
                tickers_gre_50.append(row['Ticker'])
                tickers_gre_50_bookval.append(row['Book Value'])
                tickers_gre_50_close.append(row['Close'])

            '''if(float(row['Book Value'])<0 and row['Ticker'] in tickers_gre_50):
                tickers_gre_50.remove(row['Ticker'])
                tickers_gre_50_bookval.remove(row['Book Value'])
                tickers_gre_50_close.remove(row['Close'])'''
            
    list_clubber_final_50=[tickers_gre_50,tickers_gre_50_bookval,tickers_gre_50_close]
    export_data_complete_50=zip_longest(*list_clubber_final_50,fillvalue='')

    with open(r"Auto generated Dataset\Filtered_50_percent.csv",'w',encoding="ISO-8859-1",newline="") as myfile:
        wr=csv.writer(myfile)
        wr.writerow(("Ticker","Book Value","LTP"))
        wr.writerows(export_data_complete_50)
                
    with open(r"Auto generated Dataset\Filtered_50_percent.csv",'r') as f,open('Filtered_50_percentt.csv','w') as out_file:
        out_file.writelines(unique_everseen(f))

