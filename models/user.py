from sqlmodel import SQLModel,Field,Relationship
from typing import Optional
from datetime import datetime,date
from pydantic import EmailStr
from sqlmodel import Session,select
from fastapi import Depends
from db import engine

def get_session():
        
    with Session(engine) as session:
        yield session



class User(SQLModel,table=True):
    id: Optional[int]|None =Field(primary_key=True)
    name: str
    email: EmailStr
    activation: int
    role: int
    email_verified_at: Optional[datetime] = None
    password: str
    photo_url: Optional[str] = None
    image_version: Optional[str] = None
    shop_name: Optional[str] = None
    phone_number: Optional[str] = None
    phone_number2: Optional[str] = None
    phone_number3: Optional[str] = None
    about_shop: Optional[str] = None
    credit: int
    tin: Optional[str] = None
    business_type: Optional[str] = None
    remember_token: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None  

    main_order: Optional["MainOrder"] = Relationship(back_populates="user")  



async def get_user(username,session: Session = Depends(get_session)):
    return session.exec(select(User).where(User.email==username))

