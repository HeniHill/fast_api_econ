from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class PasswordReset(SQLModel, table=True):
    email: str = Field(max_length=191, nullable=False, index=True)
    token: str = Field(max_length=191, nullable=False)
    created_at: Optional[datetime] = None
