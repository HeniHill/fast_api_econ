from typing import Union, Annotated,Optional
from passlib.context import CryptContext
from models.user import User
from pydantic import BaseModel
import jwt
from db import engine
from sqlmodel import Session,select
from sqlmodel.ext.asyncio.session import AsyncSession
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta
from fastapi import Depends,HTTPException,status,APIRouter
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pass_context=CryptContext(schemes=["bcrypt"],deprecated="auto")



router=APIRouter()

def get_session():
    
    with AsyncSession(engine) as session:
        yield session



def verify_pass(plain_pass,hashed_pass):
    return pass_context.verify(plain_pass,hashed_pass)

def hash(plain_pass):
    return pass_context.hash(plain_pass)

SECRET_KEY="62b349fa7ec4d40b06a6ee2b5105e09a23965c35c5856da40bfce21407c9e8d5c22b6c8267c812b3"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_TIME=30



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None


def get_user(username: str):
    with Session(engine) as session:
        ret= session.exec(select(User).where(User.email==username))
        try:
            return ret.one()
        except:
            return None

def authenticate_user(username: str, password: str):
    user=get_user(username)    
    if not user:
        return False
    if not verify_pass(password,user.password):
        return False
    return user


def create_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_TIME)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    cred_ex=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    try:
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is missing")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise InvalidTokenError
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise cred_ex
    user=get_user(token_data.username)
    if user is None:
        raise cred_ex
    return user 


@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(days=ACCESS_TOKEN_EXPIRE_TIME)
    access_token = create_token(
        data={"sub": user.json()}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")



    
    

