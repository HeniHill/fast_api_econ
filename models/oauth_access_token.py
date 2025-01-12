from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class OauthAccessToken(SQLModel, table=True):
    id: str = Field(primary_key=True, max_length=100)
    user_id: Optional[int] = None
    client_id: int
    name: Optional[str] = Field(default=None, max_length=191)
    scopes: Optional[str] = None
    revoked: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
