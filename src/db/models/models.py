import enum

from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship

from src.db.models.mixins import Timestamp
from src.db.models.base import Base


class Role(enum.IntEnum):
    admin = 1
    viewer = 2


class Tank(Timestamp, Base):
    __tablename__ = 'tanks'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    max_capacity = Column(Float, nullable=False)
    current_capacity = Column(Float, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)

    operation = relationship('Operation', back_populates='tank')

class Operation(Timestamp, Base):
    __tablename__ = 'operations'
    id = Column(Integer, primary_key=True, index=True)
    mass = Column(Float, nullable=False)
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    tank_id = Column(Integer, ForeignKey('tanks.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)

    tank = relationship('Tank', back_populates='operation')
    product = relationship('Product', back_populates='operation')

class Product(Timestamp, Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    operation = relationship('Operation', back_populates='product')

class User(Timestamp, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(128), index=True, nullable=False)
    password_hashed = Column(String, nullable=False)
    role = Column(Enum(Role))