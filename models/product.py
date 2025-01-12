from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime



    
class Product(SQLModel, table=True,):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_name: str = Field(max_length=191)
    user_id: int
    slug: str
    category_id: int = Field(foreign_key="category.id")
    brand: str = Field(max_length=191)
    current_price: float
    old_price: Optional[float] = None
    product_location: str = Field(max_length=191)
    availability: int
    sku: str = Field(max_length=191)
    min_order_qty: int=Field(default=1)
    tag: str=Field(default='1')
    orders: int = Field(default=0)
    visits: int = Field(default=0)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    

    # Define relationship with Category
    category: Optional["Category"] = Relationship(back_populates="products")
    order: Optional["Order"] = Relationship(back_populates="product")
    images: List["ProductImage"] = Relationship(back_populates="product")

class ProductImage(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    product_id: Optional[int] = Field(default=None, index=True,foreign_key="product.id")
    package_id: Optional[int] = Field(default=None, index=True,foreign_key="specialpackage.id")
    image_public_id: str = Field(nullable=False)
    image_version: str = Field(nullable=False)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    product: Optional[Product] = Relationship(back_populates="images")
