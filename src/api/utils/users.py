from sqlalchemy.orm import Session

from src.db.models.models import User
from src.pydantic_schemas.user import UserCreate

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, password_hashed = user.password_hashed, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return