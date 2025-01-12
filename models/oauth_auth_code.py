from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class OauthAuthCode(SQLModel, table=True):
    id: str = Field(primary_key=True, max_length=100)
    user_id: int
    client_id: int
    scopes: Optional[str] = None
    revoked: bool
    expires_at: Optional[datetime] = None
