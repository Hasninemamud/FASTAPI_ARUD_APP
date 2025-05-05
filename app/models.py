from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base  # assuming Base is defined in database.py

# User model for storing user info
# Added indexes on commonly searched fields to speed things up
class User(Base):
    __tablename__ = 'users'

    # Basic user fields
    id = Column(Integer, primary_key=True, index=True)  # always index PKs
    name = Column(String, index=True)  # might not need this index later
    email = Column(String, unique=True, index=True)  # emails should be unique
    hashed_password = Column(String)  # no index needed here
    
    
    tasks = relationship("Task", back_populates="owner")



# Task model - keeping it simple for MVP
class Task(Base):
    __tablename__ = 'tasks'  # plural by convention

    # Basic task fields 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)  # indexed for search functionality
    description = Column(String, index=True)  # probably don't need this index?
    
    # Foreign key to users table
    # Not adding ON DELETE CASCADE for now - let's see if we need it
    owner_id = Column(Integer, ForeignKey('users.id'))

    # Bi-directional relationship
    owner = relationship("User", back_populates="tasks")
    
    