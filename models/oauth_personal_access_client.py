from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class OauthPersonalAccessClient(SQLModel, table=True):
    id: int = Field(primary_key=True, autoincrement=True)
    client_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
