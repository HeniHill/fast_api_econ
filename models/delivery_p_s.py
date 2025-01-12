from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class DeliveryPS(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=191)
    phone_number: str = Field(max_length=191)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
