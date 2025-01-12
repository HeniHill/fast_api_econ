from typing import Union, Annotated
from fastapi import APIRouter, Depends,HTTPException,Request
from sqlmodel import Session,select
from models.company_setting import Company
from db import engine
from routers.appauth import hash
from routers.appauth import get_current_user
from routers.appauth import oauth2_scheme
from util.logger import log



router=APIRouter()

def get_session():
    
    with Session(engine) as session:
        yield session





@router.get("/")
@log(endpoint="/company/")
async def get_Company(session: Session = Depends(get_session),req: Request=None) -> list[Company]: 
    
    return session.exec(select(Company)).all()

@router.get("/{Company_id}")
async def get_Company_by_id(current_user: Annotated[Company,Depends(get_current_user)],Company_id: int, session: Session = Depends(get_session)) -> Company:
    """ Get an Company by id
        Then return the Company with the given id
    
    """	
    if current_user is None:
        raise HTTPException(status_code=400, detail="Inactive company")
    else:
        company= session.get(Company, Company_id)

        if company is None:
            raise HTTPException(status_code=404, detail="Company not found")
        return company

@router.post("/")
async def new_Company(company: Company, session: Session = Depends(get_session)):
    session.add(company)
    session.commit()
    session.refresh(company)
    return company