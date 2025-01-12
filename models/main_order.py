from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime



class MainOrder(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    unique_bank_code: Optional[str] = Field(default=None, max_length=191)
    order_code: str = Field(max_length=191)
    total_price: float
    discount_price: float = Field(default=0)
    delivery_price: float
    delivery_method: str = Field(max_length=191)
    payment_method: str = Field(max_length=191)
    vendor_delivery_confirmation: bool = Field(default=False)
    customer_delivery_confirmation: bool = Field(default=False)
    payment_status: bool = Field(default=False)
    order_pin: str = Field(default="0", max_length=191)
    deliveryp_id: Optional[int] = Field(default=None)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Relationship with User, assuming a User model exists
    user: Optional["User"] = Relationship(back_populates="main_order")
    order: list["Order"] = Relationship(back_populates="main_order")