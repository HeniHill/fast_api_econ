from sqlmodel import SQLModel, Field,Relationship
from typing import Optional
from datetime import datetime

class Review(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(nullable=False, index=True)
    product_id: int = Field(foreign_key="product.id",nullable=False, index=True)
    review: str = Field(default=None, nullable=False)
    rating: int = Field(nullable=False)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None



    product: "Product" = Relationship(back_populates="Review")
