from typing import Union, Annotated
from fastapi import APIRouter, Depends,HTTPException,Request
from sqlmodel import Session,select
from models.user import User
from models.otp import OTP,OTPInput
from db import engine
from routers.appauth import hash
from routers.appauth import get_current_user
from routers.appauth import oauth2_scheme
from util.logger import log
from datetime import datetime



router=APIRouter()

def get_session():
    
    with Session(engine) as session:
        yield session





@router.get("/")
@log(endpoint="/user/")
async def get_User(session: Session = Depends(get_session),req: Request=None) -> list[User]: 
    
    return session.exec(select(User)).all()

@router.get("/{User_id}")
async def get_User_by_id(current_user: Annotated[User,Depends(get_current_user)],User_id: int, session: Session = Depends(get_session)) -> User:
    """ Get an User by id
        Then return the User with the given id
    
    """	
    if current_user is None:
        raise HTTPException(status_code=400, detail="Inactive user")
    else:
        user= session.get(User, User_id)

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

@router.post("/")
async def new_User(user: User, session: Session = Depends(get_session)):
    user.password=hash(user.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user.dict(exclude={"password"})

@router.post("/validate_otp")
async def validate_otp(otp: OTPInput, session: Session = Depends(get_session)):
    otp_entry = session.exec(
    select(OTP).where(OTP.code == otp.code, OTP.phone_no == otp.phone_no)
    ).first()

    print(otp_entry)
    if otp_entry is None:
        raise HTTPException(status_code=400, status="Invalid OTP")
    if  otp_entry.date < datetime.utcnow():
        raise HTTPException(status_code=400, status="OTP expired or invalid")
    else:
        u=session.exec(select(User).where(User.phone_number == otp_entry.phone_no)).first()
        return {"status ":"success","userDate":{"phone_no":otp_entry.phone_no,"name":u.name,"email":u.email}}