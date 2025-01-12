from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Notification(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    type: str = Field(max_length=191)
    notifiable_type: str = Field(max_length=191)
    notifiable_id: int
    data: str
    read_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
