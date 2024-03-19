#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establish a connection to the MySQL database using command-line arguments
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    
    # Create a cursor object to execute SQL queries
    c = db.cursor()
    
    # Execute an SQL query to select all rows from the `states` table
    c.execute("SELECT * FROM `states`")
    
    # Iterate over the fetched rows and print each state to the console
    [print(state) for state in c.fetchall()]
