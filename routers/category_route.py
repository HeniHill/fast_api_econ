from typing import Union, Annotated
from fastapi import APIRouter, Depends,HTTPException,status
from sqlmodel import Session,select
from models.category import Category
from models.product import Product
from models.user import User
from db import engine
from routers.appauth import get_current_user



router=APIRouter()

def get_session():
    
    with Session(engine) as session:
        yield session





@router.get("/")
async def category(session: Session = Depends(get_session)) -> list[Category]: 
    
    return session.exec(select(Category)).all()

@router.get("/{category_id}")
async def get_category_by_id(current_user: Annotated[User,Depends(get_current_user)],category_id: int, session: Session = Depends(get_session)) -> Category:
    """ Get a category by id
        Then return the category with the given id
    
    """	
    category= session.get(Category, category_id)
    if caterory is None:
        raise HTTPException(status_code=404, detail="Category not found")
    else:
        return category
        
@router.get("/{category_id}/product")
async def get_category_by_id(category_id: int, session: Session = Depends(get_session)) -> list[Product]:
    """ Get a category by id
        Then return the category with the given id
    
    """	
    category= session.get(Category, category_id)
    if caterory is None:
        raise HTTPException(status_code=404, detail="Category not found")
    else:
        return category.products

@router.post("/")
async def caterory(category: Category, session: Session = Depends(get_session)):
    session.add(category)
    session.commit()
    session.refresh(category)
    return category