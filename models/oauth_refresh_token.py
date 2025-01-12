from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class OauthRefreshToken(SQLModel, table=True):
    id: str = Field(primary_key=True)
    access_token_id: str
    revoked: bool
    expires_at: Optional[datetime] = None
