import enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.orm import relationship

from src.db.models.base import Base


class Role(enum.IntEnum):
    admin = 1
    viewer = 2


class Tanks(Base):
    __tablenmae__ = 'tanks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    max_capacity = Column(Float)
    current_capacity = Column(Float)
    product_id = (Integer)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by = Integer
    modified_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_by = Integer



class Operations(Base):
    __tablenmae__ = 'operations'
    id = Column(Integer, primary_key=True)
    mass = Column(Float)
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    tank_id = Integer
    product_id = Integer
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by = Integer
    modified_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_by = Integer


class Products(Base):
    __tablenmae__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by = Integer
    modified_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_by = Integer


class Users(Base):
    __tablenmae__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password_hashed = Column(String)
    role = Column(Enum(Role))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by = Integer
    modified_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_by = Integer