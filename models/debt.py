from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class Debt(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) # Ensure `Vendor` model exists
    order_id: int = Field(foreign_key="order.id")    # Ensure `Order` model exists
    debt: int
    debt_status: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Relationships, assuming related models exist
    order: Optional["Order"] = Relationship(back_populates="debts")
