# importing module
import cx_Oracle 
  
cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\instantclient\instantclient_18_5")  
# Create a table in Oracle database
try:
  
    con = cx_Oracle.connect('hr/hr@localhost:1521/xe')
      
    # Now execute the sqlquery
    cursor = con.cursor()
      
    # Creating a table srollno heading which is number
    cursor.execute("INSERT INTO users (id , name, age) VALUES (17,'paul','49')")	
    con.commit()
    print("inserted values successfully")
      
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
  
# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()