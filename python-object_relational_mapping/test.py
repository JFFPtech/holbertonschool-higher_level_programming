import MySQLdb 
print("Connecting to database using MySQLdb") 
db_connection = MySQLdb.connect(host='DB_HOST', 
								db='DB_NAME', 
								user='DB_USERNAME', 
								passwd='DB_PASSWORD') 
print("Succesfully Connected to database using MySQLdb!") 
db_connection.close()