#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa for a given state.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306, host="localhost")
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities for the given state
    cursor.execute("SELECT cities.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s ORDER BY cities.id", (sys.argv[4],))

    # Fetch all rows and print the cities
    cities = cursor.fetchall()
    if cities:
        print(', '.join(city[0] for city in cities))
    else:
        print("No cities found for the state of", sys.argv[4])

    # Close the cursor and database connection
    cursor.close()
    db.close()
