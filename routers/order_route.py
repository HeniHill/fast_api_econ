from typing import Union, Annotated
from fastapi import APIRouter, Depends,status,HTTPException
from sqlmodel import Session,select
from models.product import Product
from models.order import Order
from models.main_order import MainOrder
from models.color import Color
from models.user import User
from db import engine
from routers.appauth import get_current_user



router=APIRouter()

def get_session():
    
    with Session(engine) as session:
        yield session





@router.get("/")
async def orders(session: Session = Depends(get_session)) -> list[MainOrder]: 
    
    return session.exec(select(MainOrder)).all()

@router.get("/{order_id}")
async def get_order_by_id(order_id: int, session: Session = Depends(get_session)) :
    """ Get an User by id
        Then return the User with the given id
    
    """
    order= session.get(MainOrder,order_id)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    else:

        return {
                 "order":order,
                 "order_details":[order.order]
                } 

@router.post("/")
async def order(order: MainOrder, session: Session = Depends(get_session)):
    session.add(order)
    session.commit()
    session.refresh(order)
    return order