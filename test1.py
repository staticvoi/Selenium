import pandas as pd
import cx_Oracle
from selenium import webdriver
from ExcelSQLMail.sendemail import sendingmail
#from sendemail import sendingmail
#from db import dbConn

print("Data from Excel sheet")
dfexcel = pd.read_excel (r'C:\Users\HP\Desktop\Selenium using python\ExcelSQLMail\data.xlsx')
print (dfexcel)


print("Unique Names")
uniqueNames = dfexcel.NAME.unique()
print(uniqueNames)

#firstName=uniqueNames[0]
#print(firstName)

for i in range(len(uniqueNames)):
  
    uniqueName = uniqueNames[i]

    position = dfexcel.loc[dfexcel.NAME == uniqueName, 'POSITION']
    finalpositions = ''
    for i in position:
        finalpositions = finalpositions +""+"," + i

    email, scholarno = dbConn(uniqueName)
    
    # the message to be emailed
    mail_content = 'Hello, '+uniqueName+" . Scholar No: "+str(scholarno) +'   Your positions in council are :'+finalpositions

    sendingmail(mail_content,email)    
