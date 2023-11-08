# importing module
import cx_Oracle 
  
cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\instantclient\instantclient_18_5")  
# Create the session pool
pool = cx_Oracle.SessionPool(user="hr", password="hr",
                             dsn="localhost:1521/xe", min=2,
                             max=5, increment=1, encoding="UTF-8")

# Acquire a connection from the pool
connection = pool.acquire()

# Use the pooled connection
cursor = connection.cursor()
for result in cursor.execute("select * from users"):
    print(result)

# Release the connection to the pool
pool.release(connection)

# Close the pool
pool.close()





'''Standalone connections

These are useful when the application maintains a single user session to a database. 
Connections are created by cx_Oracle.connect() or its alias cx_Oracle.Connection().

Pooled connections

Connection pooling is important for performance when applications frequently connect and disconnect from the database. 
Pools support Oracle’s high availability features and are recommended for applications that must be reliable. 
Small pools can also be useful for applications that want a few connections available for infrequent use. 
Pools are created with cx_Oracle.SessionPool() at application initialization time, and then SessionPool.acquire() 
can be called to obtain a connection from a pool.
'''


