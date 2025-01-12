from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class PaymentInfo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(nullable=False, index=True,foreign_key="user.id")
    merchant_code: Optional[str] = Field(default=None, max_length=191)
    pdt_token: Optional[str] = Field(default=None, max_length=191)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
