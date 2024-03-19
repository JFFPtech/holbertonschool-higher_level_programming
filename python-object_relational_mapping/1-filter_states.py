#!/usr/bin/python3
"""Module to list all states from a database"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establish a connection to the MySQL database using command-line arguments for username, password, and database name
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    
    # Create a cursor object to execute SQL queries
    c = db.cursor()
    
    # Execute an SQL query to select all rows from the `states` table, ordered by `id`
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    
    # Fetch all rows returned by the query and print each row if the name of the state starts with 'N'
    [print(state) for state in c.fetchall() if state[1][0] == "N"]

    # Close cursor and database connection
    c.close()
    db.close()
