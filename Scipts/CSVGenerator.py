'''Fetches data for all the listed stock tickers on NSE and segregates the data in csv file for each ticker automatically.'''

import yfinance as yf 
import csv

def dataset_generator():

    #-------------------------------------------------------------
    #Tickers.csv has the list of symbols of all NSE listed tickers

    comp=csv.reader(open("Prerequisites-Outputs\Tickers.csv"))     
    for c in comp:

        symbol=c[0]

        #Creation of individual CSVs for all listed tickers in Tickers.csv

        history_filename="Auto generated Dataset\{}.csv".format(symbol)  
        f=open(history_filename,'w',newline="")

        #---------------------------------------------------------------------------------
        #Data being fetched from yfinance an then being written in individual Ticker's CSV

        ticker=yf.Ticker(symbol)
        df=ticker.history(period='1mo')
        f.write(df.to_csv())
        f.close()

    print("Dataset Generation Complete")

