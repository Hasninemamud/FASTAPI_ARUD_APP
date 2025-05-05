from pydantic import BaseModel, EmailStr  # EmailStr is nice for validation
from typing import List, Optional

# Auth stuff
class Token(BaseModel):
    access_token: str
    token_type: str    # probably just "bearer" but keeping it flexible

# Base task model - keeping it simple for now
class TaskBase(BaseModel):
    title: str    # required field
    description: Optional[str] = None    # null is fine here

# For creating new tasks
class TaskCreate(TaskBase):
    owner_id: int     # foreign key to users table
    # might need to add due_date later?

# Complete task model with DB fields
class Task(TaskBase):
    id: int      # auto-incrementing primary key
    owner_id: int
    
    # needed for SQLAlchemy - remember to always add this!
    class Config:
        orm_mode = True    # lets pydantic work with ORM objects

# User related models below
class UserBase(BaseModel):
    name: str
    email: EmailStr    # nice to have email validation built-in
    
# Used when creating new users
class UserCreate(UserBase):
    password: str    # storing this separately for security
    # Note: should probably add password validation here at some point

# Full user model for responses
class User(UserBase):
    id: int
    tasks: List[Task] = []    # empty list by default
    
    class Config:
        orm_mode = True    # same as Task model

