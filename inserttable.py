# importing module
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\instantclient\instantclient_18_5")

conn = cx_Oracle.connect('hr/hr@localhost:1521/xe')
print(conn.version)
	
# Now execute the sqlquery
cursor = conn.cursor()
	
#cursor.execute("INSERT INTO student11 (rollno,name,fees,mobile) VALUES (1,'nick','2000','758757576')")	
#cursor.execute("INSERT INTO users (id , name, age) VALUES (11,'ian','29')")	

#cursor.execute("INSERT INTO council (scholarno ,name ,year ,email) VALUES (10,'Shruti','1998','shruttynair27@gmail.com')")	
#cursor.execute("INSERT INTO council (scholarno ,name ,year ,email) VALUES (12,'Prajwal','1997','shruttynair27@gmail.com')")
#cursor.execute("INSERT INTO council (scholarno ,name ,year ,email) VALUES (14,'Neha','1998','ShrutiS.Nair@lntinfotech.com')")
#cursor.execute("INSERT INTO council (scholarno ,name ,year ,email) VALUES (15,'Sundar','1999','skvmtravels@gmail.com')")
#cursor.execute("INSERT INTO council (scholarno ,name ,year ,email) VALUES (16,'Sagar','1997','skvmtravels@gmail.com')")
cursor.execute("INSERT INTO council (scholarno ,name ,year ,email) VALUES (15,'Sundar','1999','skvmtravels@gmail.com')")

conn.commit()
print("inserted values successfully")
conn.close()
