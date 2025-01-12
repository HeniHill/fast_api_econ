from db import engine,get_session
from models.log import Logs
from fastapi import Depends,Request
from datetime import datetime
from sqlmodel import Session
from functools import wraps
from decouple import config


# Samuel alemneh taye

can_log=config("LOG",cast=bool)


def log(endpoint: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(session: Session,req:Request,*args, **kwargs):
            if can_log:
                current=datetime.now()
                l=Logs(source=req.client.host,endpoint=endpoint,created_at=current)
                session.add(l)
                session.commit()
            return await func(session,req,*args, **kwargs)
        return wrapper
    return decorator


