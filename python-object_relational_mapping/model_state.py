#!/usr/bin/python3
'''defing the SQL Alchemy using a database class'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
Base = declarative_base()


class City(Base):
    '''A class that defines of a table in the sql'''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
