from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Newsletter(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(max_length=191, unique=True)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
