'''Run this script right after execution of FinancialsExtractor is finished. The objective of this script is to fix the rows with dummy data where the data was insufficiently downloaded. '''

import csv
import numpy

f=open("Auto generated Dataset\FinancialsBunch.csv","w",newline="") 

with open('Auto generated Dataset\Financials.csv',"r+") as mf:
    data=csv.DictReader(mf)
    wr=csv.writer(f)
    wr.writerow(("Ticker","Book Value","EVToEBITDA","PToBV","MarketCap","PToSales","Close","Shares Outstanding","Revenue"))

    for row in data:
       
        if(row['PToBV']=="" and row['EVToEBITDA']=="" and row['PToSales']==""):
           wr.writerow((row['Ticker'],row['Book Value'],"22222","22222",row['MarketCap'],"22222",row['Close'],row['Shares Outstanding'],row['Revenue']))

        elif(row['EVToEBITDA']=="" and row['PToBV']==""):
            wr.writerow((row['Ticker'],row['Book Value'],"22222","22222",row['MarketCap'],row['PToSales'],row['Close'],row['Shares Outstanding'],row['Revenue']))

        elif(row['EVToEBITDA']=="" and row['PToSales']==""):
            wr.writerow((row['Ticker'],row['Book Value'],"22222",row['PToBV'],row['MarketCap'],"22222",row['Close'],row['Shares Outstanding'],row['Revenue']))

        elif(row['PToBV']=="" and row['PToSales']==""):
            wr.writerow((row['Ticker'],row['Book Value'],row['EVToEBITDA'],"22222",row['MarketCap'],"22222",row['Close'],row['Shares Outstanding'],row['Revenue']))

        elif(row['PToBV']==""):
           wr.writerow((row['Ticker'],row['Book Value'],row['EVToEBITDA'],"22222",row['MarketCap'],row['PToSales'],row['Close'],row['Shares Outstanding'],row['Revenue']))

        elif(row['EVToEBITDA']==""):
           wr.writerow((row['Ticker'],row['Book Value'],"22222",row['PToBV'],row['MarketCap'],row['PToSales'],row['Close'],row['Shares Outstanding'],row['Revenue']))

        elif(row['PToSales']==""):
           wr.writerow((row['Ticker'],row['Book Value'],row['EVToEBITDA'],row['PToBV'],row['MarketCap'],"22222",row['Close'],row['Shares Outstanding'],row['Revenue']))

        else:
           wr.writerow((row['Ticker'],row['Book Value'],row['EVToEBITDA'],row['PToBV'],row['MarketCap'],row['PToSales'],row['Close'],row['Shares Outstanding'],row['Revenue']))

