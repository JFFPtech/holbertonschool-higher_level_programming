#!/usr/bin/python3
"""Lists all states starting with 'N' from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to fetch states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    # Fetch all rows using fetchall() method
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
