from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime



class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    package_id: Optional[int] = Field(default=None)
    order_code: str = Field(max_length=191)
    quantity: int
    paid_amount: Optional[float] = Field(default=None)
    color_id: Optional[int] = Field(default=None, foreign_key="color.id")
    main_order_id: int = Field(foreign_key="mainorder.id")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Relationships with other models
    product: Optional["Product"] = Relationship(back_populates="order")
    color: Optional["Color"] = Relationship(back_populates="order")
    main_order: Optional["MainOrder"] = Relationship(back_populates="order")