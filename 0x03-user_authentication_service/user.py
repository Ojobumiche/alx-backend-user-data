#!/usr/bin/env python3
"""User module
"""
from sqlalchemy.ext.declarative import DeclarativeBase
from sqlalchemy import Column, Integer, String

Base = DeclarativeBase()

""" This defined a User class
"""
class User(Base):
    
    """ This is a table name
    """
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True),
    email =Column(String(25), nullable=False),
    hashed_password = Column(String(25), nullable=False),
    session_id = Column(String(25), nullable=False),
    reset_token = Column(String(25), nullable=False)
    
    
    def  __repr__(self):
        """
        String rep.
        """
        return f"User: 1d={self.id}"

