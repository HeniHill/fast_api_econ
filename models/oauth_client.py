from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class OauthClient(SQLModel, table=True):
    id: int = Field(primary_key=True, autoincrement=True)
    user_id: Optional[int] = None
    name: str
    secret: str
    redirect: str
    personal_access_client: bool
    password_client: bool
    revoked: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
