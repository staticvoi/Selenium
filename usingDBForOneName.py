import pandas as pd
import cx_Oracle
from selenium import webdriver
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart

dfexcel = pd.read_excel (r'C:\Users\HP\Desktop\Selenium using python\ExcelSQLMail\data.xlsx')
print (dfexcel)

uniqueNames = dfexcel.NAME.unique()
print(uniqueNames)

firstName=uniqueNames[0]
print(firstName)

position = dfexcel.loc[dfexcel.NAME == firstName, 'POSITION']
finalpositions = ''
for i in position:
    finalpositions = finalpositions +""+"," + i
print(finalpositions)




cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\instantclient\instantclient_18_5")

conn = cx_Oracle.connect('hr/hr@localhost:1521/xe')
#print(conn.version)
	
cursor = conn.cursor()
sql = "select * from council where NAME = :NAME"
cursor.execute(sql, NAME=firstName)
row = cursor.fetchone()
print(row)

email = row[3]
scholarno = row[0]

mail_content = 'Hello, '+firstName+' Your positions in council are :'+finalpositions

msg = MIMEMultipart()
  
password = "skvm@123"
msg['From'] = "skvmtravels@gmail.com"

msg['To'] = email
msg['Subject'] = "Scholar No: "+str(scholarno)

msg.attach(MIMEText(mail_content, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
server.login(msg['From'], password)
 
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print("successfully sent email to %s" % (msg['To']))
