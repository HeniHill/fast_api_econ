from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class SpecialOffer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Relationship with Product, assuming a Product model exists
    product: Optional["Product"] = Relationship(back_populates="SpecialOffer")
