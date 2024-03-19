import sys
import MySQLdb

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute the SQL query to retrieve unique states
    cursor.execute("SELECT DISTINCT * FROM `states` WHERE id IN (4, 5)")

    # Fetch all rows and print each state
    for state in cursor.fetchall():
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
