# importing module
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\instantclient\instantclient_18_5")

conn = cx_Oracle.connect('hr/hr@localhost:1521/xe')
#print(conn.version)
	
# Now execute the sqlquery
cursor = conn.cursor()
	
#cursor.execute("SELECT * FROM student11")
#cursor.execute("SELECT * FROM users")
cursor.execute("SELECT * FROM council")
#row = cursor.fetchone()	
row = cursor.fetchall()	
while row:
    print(row)
    row = cursor.fetchone()
#print("inserted values successfully")
conn.close()
