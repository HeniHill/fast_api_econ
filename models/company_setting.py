from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str = Field(max_length=191)
    slug: Optional[str] = None
    location: str = Field(max_length=191)
    phone_number: str = Field(max_length=191)
    email: str = Field(max_length=191)
    facebook: Optional[str] = None
    twitter: Optional[str] = None
    google_plus: Optional[str] = None
    instagram: Optional[str] = None
    products_amount_for_discount: int
    discount: Optional[float] = None
    delivery_per_km: Optional[int] = None
    address: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    cut_business: Optional[float] = None
    cut_individual: Optional[float] = None
    shipping_guide: Optional[str] = None
    shipping_return: Optional[str] = None
    about: Optional[str] = None
    terms_and_condition: Optional[str] = None
    credit_hint: Optional[str] = None
    online_payment_limit: Optional[float] = None
    symmart_standard_price: float = Field(default=50)
    symmart_premium_price: float = Field(default=150)
    symmart_national_price: float = Field(default=200)
    symmart_express_price: float = Field(default=100)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
