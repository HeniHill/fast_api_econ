from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class NewsletterTheLetters(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=191)
    slug: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
