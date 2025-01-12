from sqlmodel import SQLModel, Field
from typing import Optional
from time import datetime

class PackageProduct(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, nullable=False)
    product_id: int = Field(foreign_key="product.id", nullable=False)
    package_id: int = Field(foreign_key="package.id", nullable=False)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
