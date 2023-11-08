# importing module
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\instantclient\instantclient_18_5")

conn = cx_Oracle.connect('hr/hr@localhost:1521/xe')
print(conn.version)
	
# Now execute the sqlquery
cursor = conn.cursor()
cursor.execute("create table users(id number, name varchar2(10), age number(3))")

conn.commit()                  
print("Table Created successfully")
conn.close()
