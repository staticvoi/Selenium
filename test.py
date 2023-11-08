import pandas as pd
import cx_Oracle
from selenium import webdriver
from ExcelSQLMail.sendemail import sendingmail
#from sendemail import sendingmail


dfexcel = pd.read_excel (r'C:\Users\HP\Desktop\Selenium using python\ExcelSQLMail\data.xlsx')
print (dfexcel)

uniqueNames = dfexcel.NAME.unique()
print(uniqueNames)

#firstName=uniqueNames[0]
#print(firstName)


cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\instantclient\instantclient_18_5")

conn = cx_Oracle.connect('hr/hr@localhost:1521/xe')
#print(conn.version)
	
cursor = conn.cursor()

for i in range(len(uniqueNames)):
  
    uniqueName = uniqueNames[i]

    position = dfexcel.loc[dfexcel.NAME == uniqueName, 'POSITION']
    finalpositions = ''
    for i in position:
        finalpositions = finalpositions +""+"," + i

    sql = "select * from council where NAME = :NAME"
    cursor.execute(sql, NAME=uniqueName)
    row = cursor.fetchone()
    print(row)

    email = row[3]
    #emaillist = ''
    #emaillist = emaillist.append(email)
    #print(emaillist)
    scholarno = row[0]
    print(email)
    #print(type(email))
    
    # the message to be emailed
    mail_content = 'Hello, '+uniqueName+"Scholar No: "+str(scholarno) +'   Your positions in council are :'+finalpositions

    sendingmail(mail_content,email)    
