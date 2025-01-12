from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel



class OTP(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    phone_no: str
    code:str
    valid:bool=Field(nullable=False,default=True)
    date:datetime=Field(nullable=False,default=datetime.now())

# OTP Input Model for Request Body
class OTPInput(BaseModel):
    phone_no: str
    code: str    