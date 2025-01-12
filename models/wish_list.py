from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class WishList(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    product_id: int = Field(nullable=False, index=True,foreign_key="product.id")
    user_id: int = Field(nullable=False, index=True)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
