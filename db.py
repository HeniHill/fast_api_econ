from sqlmodel import  SQLModel,create_engine,Session


DB_URL="mysql://root:@localhost/fast" 

engine=create_engine(DB_URL)


def get_session():
        
    with Session(engine) as session:
        yield session