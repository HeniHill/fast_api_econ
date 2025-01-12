from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class Address(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    address: str = Field(max_length=191)
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Assuming a User model exists, establish a relationship
    user: Optional["User"] = Relationship(back_populates="addresses")
