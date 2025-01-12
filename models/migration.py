from sqlmodel import SQLModel, Field
from typing import Optional

class Migrations(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    migration: str = Field(max_length=191)
    batch: int
