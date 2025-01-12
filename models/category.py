from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    category_name: str = Field(max_length=191)
    image_public_id: str = Field(max_length=191)
    image_version: str = Field(max_length=191)
    image_url: str = Field(max_length=191)
    parent_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Define relationship with Product
    products: List["Product"] = Relationship(back_populates="category")

    
