import random
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class MiniatureBase(BaseModel):
    name: str
    description: Optional[str]
    image_url: Optional[str]


class MiniatureCreate(MiniatureBase):
    id: int = random.randint(1, 9999)
    pass


class MiniatureUpdate(MiniatureBase):
    id: int
    pass


class Miniature(MiniatureBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    pass


class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
