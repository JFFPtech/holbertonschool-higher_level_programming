#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Creating the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Creating a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Creating a session
    session = Session()

    # Querying all State objects and sorting by id
    states = session.query(State).order_by(State.id).all()

    # Printing the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Closing the session
    session.close()
