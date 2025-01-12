from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Contact(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fullname: str = Field(max_length=191)
    email: str = Field(max_length=191)
    subject: str = Field(max_length=191)
    message: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
