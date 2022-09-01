# D&V's Finance Wizard 
![](https://i.imgur.com/waxVImv.png) 

![Capture1](https://user-images.githubusercontent.com/78873223/188002666-57db1f7d-d218-4e30-a44b-1c93b9c05d86.PNG)
![Capture](https://user-images.githubusercontent.com/78873223/188002660-f481b318-d9fa-46b9-b817-eee6d0641315.PNG)

![](https://i.imgur.com/waxVImv.png)
## This is a finance repository that currently does the following:


1}Data fetching for Stocks listed on NSE India with automatic csv generation for individual ticker.(CSVGenerator.py)

      1.1 -> List of tickers available (Tickers.csv)

      1.2 -> Garbage Collector is prepared to filter out delisted companies from the stock exchange (GarbageCollector.py)
      

2}CandleStick Pattern Recognition with involvement of multiple technical indicators to build a basic coded trading strategy.  (talibtest.py,PatternRecognition.py)
      
      2.1 -> Outputs a csv file with ticker name indicating the specific pattern formed. (BullishEngufing.csv,BearishEngufing.csv,Gravestone.csv)


3}Financials Data Extraction at a single click for all the listed tickers using Thread Pool Executors.(FinancialsExtractor.py)
    
      3.1 -> List of tickers available (Tickers.csv)
      
      3.2 -> Outputs a csv file with all the financial data for individual tickers fetched from Yahoo Finance. (Financials.csv)
      
      3.3 -> Garbage collector is prepared to fix the the rows containing insufficient data in the output csv file to avoid interruptions in processing later. (FinancialsGarbageCollector.py)
        
             3.3.1 -> Outputs a csv file with complete data after fixing the previous output csv file. (FinancialsBunch.csv)
             

4} Fundamental Screening of stocks to sort the undervalued list of stocks based on three criterias: 

      4.1 -> Picks the list of stocks that are trading n% below their book value where n is variable indicating amount of percentage. (FundamentalScreener.py)
      
             4.1.1 -> Outputs a csv file containing the financial data of the filtered stocks. (Filtered_50_percent.csv)
             
      4.2 -> Picks the list of stocks that are trading with PriceToSales ratio of below 1.25. (FundamentalScreener3.py)
      
             4.2.1 -> Outputs a csv file containing the financial data of the filtered stocks. (MCapPTS.csv)
             
      4.3 -> Picks the list of stocks that are trading with EV/EBITDA ratio ranging in 0.1 - 10.9 (evebitda_screening.py)
      
             4.3.1 -> Outputs a csv file containing the financial data of the filtered stocks. (EVToEbitda_Output.csv)
             

5} Chart Plotting Demo for stocks using Cufflinks Library including involvement of technical indicators (Cuffinks Demo.py):

      5.1 -> Outputs a technical chart for specified tickers with specified parameters.
      

6}Valutation determiner from all the ticker's data available in FinancialsBunch.csv based on following criterias (Valuation.py):

      -> Book Value Per Share
      -> Annual Sales
      
      6.1 -> Outputs a csv file containing the valuations for all the stocks as per their book value, annual sales. (Valuations.csv)
      

7} Screening of stocks present in Valuations.py to spot the ones trading at a discount (DiscountValuations.py):

      7.1 -> Outputs a csv file containing name of tickers trading at a discount along with amount of discount(%) based on their BookValue (Discount_BookValue.csv)
      
      7.2 -> Outputs a csv file containing name of tickers trading at a discount along with amount of discount(%) based on their annual sales (Discount_Sales.csv)


8} Provision to mail the necessary output files at a single click is available. (Mailer.py)


---

![](https://i.imgur.com/waxVImv.png)
### Note:


### Before beginning, place the Tickers.csv from Scripts directory to Auto Generated Dataset directory as it got truncated due to large amount of dataset generated initially. 

Before executing the scripts, make sure to turn on 'Less Secure App access' option from your gmail ID that will be used to send out the mails. To do so, get going with the following steps:

> 1.Log into the Gmail account that will be used to send the emails.

> 2.Go to Gmail's [Less Secure App Access](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NELkm6zvkeSQxzOL8a2UdhbIUASi6uvDQY573YvLX9rO1G5GHA4Um6YgEmGmZD6_Jc2tsqRDXuMf99mMud0Pslsov5MA)

> 3.Set the Allow less secure apps option to ON.


![](https://i.imgur.com/waxVImv.png)
## Libraries to be installed:


> 1. yfinance
> 2. yahoofinancials
> 3. numpy
> 4. more-itertools
> 5. pandas
> 6. talib
> 7. cufflinks

### Installation can be done using the pip command. (Example: pip install pandas)

![](https://i.imgur.com/waxVImv.png)
## Inbuilt libraries required:


> 1. datetime
> 2. csv
> 3. os
> 4. smtplib
> 5. itertools
> 6. concurrent.futures
> 7. math
> 8. traceback
> 9. mimetypes


