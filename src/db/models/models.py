import enum

from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship

from src.db.models.mixins import Timestamp
from src.db.models.base import Base


class Role(enum.IntEnum):
    admin = 1
    viewer = 2

class User(Timestamp, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(128), unique=True, index=True, nullable=False)
    password_hashed = Column(String(255), nullable=False)
    role = Column(Enum(Role))
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    modified_by = Column(Integer, ForeignKey('users.id'), nullable=False)


class Tank(Timestamp, Base):
    __tablename__ = 'tanks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    max_capacity = Column(Float, nullable=False)
    current_capacity = Column(Float, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    modified_by = Column(Integer, ForeignKey('users.id'), nullable=False)

    product = relationship("Product", back_populates="tanks")
    operations = relationship("Operation", back_populates="tank")


class Operation(Timestamp, Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True, index=True)
    mass = Column(Float, nullable=False)
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    tank_id = Column(Integer, ForeignKey('tanks.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    modified_by = Column(Integer, ForeignKey('users.id'), nullable=False)

    tank = relationship("Tank", back_populates="operations")
    product = relationship("Product", back_populates="operations")


class Product(Timestamp, Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    modified_by = Column(Integer, ForeignKey('users.id'), nullable=False)

    tanks = relationship("Tank", back_populates="product")
    operations = relationship("Operation", back_populates="product")




