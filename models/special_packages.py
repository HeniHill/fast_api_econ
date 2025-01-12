from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime



class SpecialPackage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    package_name: str = Field(unique=True, max_length=191)
    discount_price: float
    discount_percent: float
    availability: int
    slug: str
    user_id: int = Field(foreign_key="user.id")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Relationship with User, assuming a User model exists
    user: Optional["User"] = Relationship(back_populates="SpecialPackage")