from numpy import unique
import numpy as np
import pandas as pd
import cx_Oracle 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

print('DF of Excel sheet')
dfexcel = pd.read_excel (r'C:\Users\HP\Desktop\Selenium using python\ExcelSQLMail\data.xlsx')
print (dfexcel)

#print(df['Name'])
#print(df['Name'].unique())
#print(list(set(df['Name'])))

#namesInExcel = list(set(dfexcel['NAME']))
#print(namesInExcel)


cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\instantclient\instantclient_18_5")  
# Create the session pool
pool = cx_Oracle.SessionPool(user="hr", password="hr", dsn="localhost:1521/xe", min=2,max=5, increment=1, encoding="UTF-8")

# Acquire a connection from the pool
connection = pool.acquire()

# Use the pooled connection
#cursor = connection.cursor()
#dataInDB = cursor.execute("select * from council where NAME=namesInExcel")
#print(dataInDB)


print('DF from DB is: ')
dfDB = pd.read_sql('select * from council',connection)
print(dfDB)
# Release the connection to the pool
pool.release(connection)
# Close the pool
pool.close()

#dataInDB.to_excel(r'C:\Users\HP\Desktop\Selenium using python\ExcelSQLMail\council.xlsx')

#dfsql = pd.read_excel(r'C:\Users\HP\Desktop\Selenium using python\ExcelSQLMail\council.xlsx')
#print(dfsql)

#namesInDB = list(set(dfsql['NAME']))
# print(namesInDB)

print('After merging both DB and excel Tables')
dffinal = pd.merge(dfexcel, dfDB, on='NAME')
#dffinal = pd.concat([dfsql,dfexcel])
print(dffinal)
#dffinal.reset_index(drop=True)

print('Unique Names in merged table are')
uniqueNames = dffinal['NAME'].unique()
print(uniqueNames)
#print(dffinal.columns.values.tolist())

for i in range(len(uniqueNames)):
    dataOfPeople = dffinal[['POSITION', 'SCHOLARNO', 'EMAIL']].where(dffinal['NAME'] == uniqueNames[i])
    #dataOfPeople.dropna(subset = ['POSITION', 'SCHOLARNO', 'EMAIL'], how='all')
    print(dataOfPeople)
    emailNAN = dataOfPeople['EMAIL'].unique()
    print(emailNAN)
    if i == 0:
        email = np.delete(emailNAN,-1)
    else:
        email = np.delete(emailNAN,0)
    print(email)
    finalemail = np.array_str(email)
    finalemail = finalemail.strip()
    print(finalemail)
    print(type(finalemail))
    print(len(finalemail))
    

    scholarnoNAN = dataOfPeople['SCHOLARNO'].unique()
    #print(scholarno)
    if i == 0:
        scholarno = np.delete(scholarnoNAN,-1)
    else:
        scholarno = np.delete(scholarnoNAN,0)
    print(scholarno)

    positionNAN = dataOfPeople['POSITION'].unique()
    if i == 0:
        position = np.delete(positionNAN,-1)
    else:
        position = np.delete(positionNAN,0)
    print(position)
    finalposition = np.array_str(position)
    print(finalposition)
    #print(type(finalposition))
    

    mail_content = 'Hello '+' , The details of your council position are as below: '+ finalposition
    # create message object instance
    msg = MIMEMultipart()
    
    # setup the parameters of the message
    password = "skvm@123"
    msg['From'] = "skvmtravels@gmail.com"
    #msg['To'] = "shruttynair27@gmail.com"
    msg['To'] = finalemail
    msg['Subject'] = "Your Scholar No is :"+ str(scholarno)
    
    # add in the message body
    msg.attach(MIMEText(mail_content, 'plain'))
    
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    
    
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    server.quit()
    
    print("successfully sent email to %s" % (msg['To']))
