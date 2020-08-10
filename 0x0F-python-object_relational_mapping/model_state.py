#!/usr/bin/python3
"""Python file that contains the class definition of a State
and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class definition based in Base instance"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(128), nullable=False)
