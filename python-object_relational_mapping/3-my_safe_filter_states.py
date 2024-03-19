#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
where name matches the argument, using safe parameterized queries.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all command-line arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Establish a connection to the MySQL database
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
        cursor = db.cursor()

        # Execute the SQL query using parameterized query to prevent SQL injection
        cursor.execute("SELECT * FROM `states` WHERE `name` = %s ORDER BY `id`", (state_name,))

        # Fetch all rows returned by the query and print each row
        for row in cursor.fetchall():
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'db' in locals() and db is not None:
            db.close()
