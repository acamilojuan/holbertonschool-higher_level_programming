#!/usr/bin/python3
"""Script that prints the State object with
the name passed as argument from the database"""
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

    new_state = State()
    new_state.name = 'Louisiana'
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
