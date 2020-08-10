#!/usr/bin/python3
"""Script that lists all State objects that contain
the letter a from the database"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Engine creation"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_list = session.query(State).filter(State.name.contains("a"))

    for state in states_list:
        print("{}: {}".format(state.id, state.name))

    session.close()
