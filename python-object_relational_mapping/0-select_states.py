#!/usr/bin/python3
""" Python3 Script used to list all states from the database hbtn_0e_0_usa """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                        user=username, passwd=password, db=database)
    
    # Creates a cursor
    cursor = db.cursor()

    # Executes the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch all the rows in a list of lists
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    # Close the cursor and database
    cursor.close()
    db.close()