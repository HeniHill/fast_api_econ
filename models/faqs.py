from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class FAQS(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    question: str
    answer: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
