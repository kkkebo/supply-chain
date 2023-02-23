from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    role: Enum


class UserCreate(UserBase):
    password_hashed: str


class User(UserBase):
    id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True