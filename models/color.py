from sqlmodel import SQLModel, Field,Relationship
from typing import Optional
from datetime import datetime

class Color(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    colour_name: str = Field(max_length=191)
    hex: str = Field(max_length=191)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    order: Optional["Order"] = Relationship(back_populates="color")
