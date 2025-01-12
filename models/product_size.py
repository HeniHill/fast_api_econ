from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class ProductSize(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    product_id: int = Field(nullable=False, index=True,foreign_key="product.id")
    size: str = Field(max_length=191, nullable=False)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
