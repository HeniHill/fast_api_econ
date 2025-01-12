from typing import Union, Annotated
from fastapi import APIRouter, Depends,status,HTTPException,Query
from sqlmodel import Session,select
from sqlalchemy.orm import selectinload
from models.product import Product,ProductImage
from typing import List

from models.user import User
from db import engine
from routers.appauth import get_current_user



router=APIRouter()

def get_session():
    
    with Session(engine) as session:
        yield session



@router.get("/")
async def procust(session: Session = Depends(get_session)): 
    
    #product= session.exec(select(Product)).all()
    cmd=select(Product).options(selectinload(Product.images))
    products= session.exec(cmd).all()
    product_with_image=[
        {
            **product.dict(),
            "image_url": [image.image_public_id for image in product.images]
        }
        for product in products
    ]
    
    
    return product_with_image

@router.get("/{procust_id}")
async def get_procust_by_id(procust_id: int, session: Session = Depends(get_session)):
    """ Get an User by id
        Then return the User with the given id
    
    """

    product=session.get(Product, procust_id)

    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    else:
        product_with_image=[
        {
            **product.dict()
        }
        ]
        return product_with_image

@router.post("/")
async def product(procust: Product, session: Session = Depends(get_session)):
    session.add(procust)
    session.commit()
    session.refresh(procust)
    return procust

@router.get("/filter/tag")
def filter_products_by_tags(
    t: str = Query(..., title="Tag", description="Tag to filter products by"),
    session: Session = Depends(get_session)
):
    statement = select(Product).where(Product.tag.contains([t]))
    products = session.exec(statement).all()
    return  products