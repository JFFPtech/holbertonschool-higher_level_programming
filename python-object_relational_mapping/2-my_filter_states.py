#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
where name matches the argument.

"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establish a connection to the MySQL database using command-line arguments for username, password, and database name
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    
    # Create a cursor object to execute SQL queries
    c = db.cursor()
    
    # Execute an SQL query to select all rows from the `states` table where the name matches the argument
    c.execute("SELECT * FROM `states` WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    
    # Fetch all rows returned by the query and print each row
    [print(state) for state in c.fetchall()]

    # Close cursor and database connection
    c.close()
    db.close()
