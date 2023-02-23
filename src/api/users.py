from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.db_setup import get_session
from src.pydantic_schemas.user import UserCreate, User
from src.api.utils.users import get_user, get_users, create_user

router = fastapi.APIRouter()

@router.get("/users", response_model=List[User])
def read_users(db: Session = Depends(get_session), skip: int = 0, limit: int = 100):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.get('/user/{user_id}', response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_session)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
