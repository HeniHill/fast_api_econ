from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Logs(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    source:Optional[str] =Field(default=None)
    endpoint:Optional[str]=None
    created_at: Optional[datetime] = None
