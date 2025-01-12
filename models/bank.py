from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class Bank(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    bank_name: str = Field(max_length=191)
    bank_account: str = Field(max_length=191)
    user_id: int = Field(foreign_key="user.id")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Assuming a User model exists, establish a relationship
    user: Optional["User"] = Relationship(back_populates="banks")
