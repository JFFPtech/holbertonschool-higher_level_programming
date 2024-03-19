#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    # Extract command-line arguments: username, password, and database name
    u_name = argv[1]
    psw = argv[2]
    base = argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=u_name, passwd=psw, db=base, port=3306)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute a MySQL query to select distinct rows from the states table, ordered by id
    cur.execute("SELECT DISTINCT * FROM states ORDER BY id")

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
