from typing import Union
from fastapi import FastAPI, Depends,Request
from sqlmodel import Session,select
from db import engine
from routers import api_route,category_route,product_route,appauth,order_route,company_route
from routers.appauth import get_current_user
from fastapi.responses import RedirectResponse

import logging

logging.basicConfig(level=logging.INFO)


app=FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):

    logging.info(f"Headers: {request.headers}")
   
    # Log the request body if it's JSON (handling for async read)
    body = await request.body()
    if body:
        logging.info(f"Body: {body.decode('utf-8')}")

    # Process the request
    response = await call_next(request)
    
    return response


app.include_router(appauth.router,prefix="/api",tags=["Token"])
app.include_router(api_route.router,prefix="/user",tags=["User"])
#app.include_router(category_route.router,prefix="/category",dependencies=[Depends(get_current_user)],tags=["Category"])
app.include_router(category_route.router,prefix="/category",tags=["Category"])
app.include_router(product_route.router,prefix="/product",tags=["Product"])
app.include_router(order_route.router,prefix="/order",tags=["Order"])
app.include_router(company_route.router,prefix="/company",tags=["Company"])


@app.get("/")
async def get_User(): 
    return RedirectResponse(url="/docs")
    


