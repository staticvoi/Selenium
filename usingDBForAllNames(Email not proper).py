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

#firstName=uniqueNames[0]
#print(firstName)


cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\instantclient\instantclient_18_5")

conn = cx_Oracle.connect('hr/hr@localhost:1521/xe')
#print(conn.version)
	
cursor = conn.cursor()

msg = MIMEMultipart()
  
password = "skvm@123"
msg['From'] = "skvmtravels@gmail.com"

server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
server.login(msg['From'], password)


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
    
    msg['To'] = email
    msg['Subject'] = "Info regarding your council details"

    # the message to be emailed
    mail_content = 'Hello, '+uniqueName+"Scholar No: "+str(scholarno) +'   Your positions in council are :'+finalpositions
    
    msg.attach(MIMEText(mail_content, 'plain'))
 
    server.sendmail(msg['From'], msg['To'], msg.as_string())

 
server.quit()
 
print("successfully sent email to %s" % (msg['To']))
