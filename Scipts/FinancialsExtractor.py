from yahoofinancials import YahooFinancials
import csv
import concurrent.futures
import yfinance as yf 
from datetime import date
from itertools import zip_longest
import numpy

'''Line 110-161 are required as backup only in case the close values are being not fetched correctly.'''

symbol=0
remover=list()
tickers_list=list()

comp=csv.reader(open("Auto generated Dataset\Tickers.csv"))

for c in comp:
    tickers_list.extend(c)

def book_value_computer(ticker):

        try:
            #d=date.today()
            #d1=d.strftime('%Y-%m-%d')

            yahoo_financials=YahooFinancials(ticker)
            hold=yahoo_financials.get_key_statistics_data()
            hold2=yahoo_financials.get_summary_data()
            hold3=yahoo_financials.get_financial_stmts('annual', 'income')
            book_value=hold[ticker]['bookValue']
            EVtoEBITDA=hold[ticker]['enterpriseToEbitda']
            priceToBookR=hold[ticker]['priceToBook']
            market_cap=(hold2[ticker]['marketCap'])//10000000
            priceToSales=(hold2[ticker]['priceToSalesTrailing12Months'])
            previous_Close=(hold2[ticker]['previousClose'])
            sharesOutstanding=hold[ticker]['sharesOutstanding']
            total_revenue=hold3["incomeStatementHistory"][ticker][0]['2021-03-31']['totalRevenue']
            #print(book_value)    
            #print("\n")

        except:
            remover.append(ticker)
            print(remover)
        
        try:
            return ticker,book_value,EVtoEBITDA,priceToBookR,market_cap,priceToSales,previous_Close,sharesOutstanding,total_revenue
        except:
            return ticker,None,None,None,None,None,None,None,None

with concurrent.futures.ThreadPoolExecutor() as executor:
 
    tickers=tickers_list[700:1243]
    results=executor.map(book_value_computer,tickers)

    ticker_results=list()
    tickers_book_value=list()
    tickers_evtoebitda=list()
    tickers_priceToBook=list()
    tickers_close=list()
    tickers_marketcap=list()
    tickers_priceToSales=list()
    tickers_sharesoutstanding=[]
    tickers_total_revenue=[]

    for result in results:
             
                ticker_results.append(result[0])
                tickers_book_value.append(result[1])
                tickers_evtoebitda.append(result[2])
                tickers_priceToBook.append(result[3])
                tickers_marketcap.append(result[4])
                tickers_priceToSales.append(result[5])
                tickers_close.append(result[6])
                tickers_sharesoutstanding.append(result[7])
                tickers_total_revenue.append(result[8])

                #tickers_close.append(result[2])

                #print(ticker_results)
                #print(tickers_book_value)
                #print(tickers_evtoebitda)
                #print(tickers_priceToBook)
                #print(tickers_close)
#print("\n")
#print("Final Outcome: ---------------------------------------------------------------------------------------------------")
#print("\n")
#print(ticker_results)
#print(tickers_book_value)
#print(tickers_evtoebitda)
#print(tickers_priceToBook)
#print(tickers_marketcap)
#print(tickers_close)

list_clubber=[ticker_results,tickers_book_value,tickers_evtoebitda,tickers_priceToBook,tickers_marketcap,tickers_priceToSales,tickers_close,tickers_sharesoutstanding,tickers_total_revenue]
export_data=zip_longest(*list_clubber,fillvalue='')

with open("Auto generated Dataset\Financials.csv",'a',encoding="ISO-8859-1",newline='') as myfile:
    wr=csv.writer(myfile)
    #wr.writerow(("Ticker","Book Value"))
    wr.writerows(export_data)
myfile.close()

holder=list()

with open("Auto generated Dataset\Financials.csv",'r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        holder.append(row)
        if not row[1]:
            holder.remove(row)

with open("Auto generated Dataset\Financials.csv",'w',newline='') as fw:
    writer=csv.writer(fw)
    writer.writerows(holder) 
print("Success")


'''ticker_names_reader=list()
ticker_book_values_reader=list()
ticker_evToEBITDA_reader=list()
ticker_priceToBook_reader=list()
ticker_marketcap=list()

with open("Auto generated Dataset\Financials.csv",'r') as csvfile:
 data = csv.DictReader(csvfile)
 print("---------------------------------")
 for row in data:
   ticker_names_reader.append(row['Ticker'])
   ticker_book_values_reader.append(row['Book Value'])
   ticker_evToEBITDA_reader.append(row['EV/EBITDA'])
   ticker_priceToBook_reader.append(row['P/BV'])
   ticker_marketcap.append(row["MarketCap"])
   

#print(ticker_names_reader)
#print(ticker_book_values_reader)

recent_closes=list() 

with open("Auto generated Dataset\Financials.csv",'r') as file1:
    csvreaderf=csv.reader(file1)
    for row in csvreaderf:
        if(row[0]=='Ticker'):
            continue 
        symbol=row[0]
        print(symbol)

        with open("Auto generated Dataset\{}.csv".format(symbol),'r') as file2:
            csv_inner_object=csv.reader(file2)
            hold=list()
            for line in csv_inner_object:
                hold.append(line[0:6])
            hold=hold[-1:]

            hold=numpy.column_stack(hold)
            close_type_nd=hold[4].astype(float)
            #print(type(close_type_nd))
            close_list=close_type_nd.tolist()
            recent_closes.extend(close_list)
    #print(recent_closes)

list_clubber_final=[ticker_names_reader,ticker_book_values_reader,ticker_evToEBITDA_reader,ticker_priceToBook_reader,recent_closes,ticker_marketcap]
export_data_complete=zip_longest(*list_clubber_final,fillvalue='')

with open("Auto generated Dataset\Financials.csv",'w',encoding="ISO-8859-1",newline='') as myfile:
    wr=csv.writer(myfile)
    wr.writerow(("Ticker","Book Value","EV/EBITDA","P/BV","Close","MarketCap"))
    wr.writerows(export_data_complete)
myfile.close()
'''




























'''holder=list()

with open('Financials.csv','r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        holder.append(row)
        if not row[1]:
            holder.remove(row)

with open('Financials.csv','w',newline='') as fw:
    writer=csv.writer(fw)
    writer.writerows(holder)'''


            

            



        
    
        



'''ticker="ADANITRANS.NS"
yahoo_financials=YahooFinancials(ticker)
hold=yahoo_financials.get_key_statistics_data()
print(hold)

print(hold['ADANITRANS.NS']['bookValue'])'''


