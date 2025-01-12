from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class ProductReview(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    review_id: int = Field(nullable=False, index=True,foreign_key="review.id")
    product_id: int = Field(nullable=False, index=True,foreign_key="product.id")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
