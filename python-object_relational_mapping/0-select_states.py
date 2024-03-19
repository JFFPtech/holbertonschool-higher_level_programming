import sys
import MySQLdb

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute the SQL query to retrieve all rows from the `states` table
    cursor.execute("SELECT * FROM `states`")

    # Create a set to store printed states
    printed_states = set()

    # Fetch all rows and print each state
    for state in cursor.fetchall():
        # Check if the state has been printed before
        if state[1] not in printed_states:
            print(state)
            # Add the state to the set of printed states
            printed_states.add(state[1])

    # Close the cursor and database connection
    cursor.close()
    db.close()
