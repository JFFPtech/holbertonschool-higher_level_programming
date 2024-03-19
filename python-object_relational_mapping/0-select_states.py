#!/usr/bin/python3
""" Python3 Script used to list all states from the database hbtn_0e_0_usa """

import sys
from sys import argv
import MySQLdb

if __name__ == "__main__":
    
    if len(argv) != 4:
        sys.exit('Usage: 0-select_states.py <username> <password> <database_name>')
    
conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")

cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()