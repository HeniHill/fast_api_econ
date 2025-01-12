from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class HomeCarousels(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    category_id: int
    image_public_id: str = Field(max_length=191)
    image_version: str = Field(max_length=191)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
