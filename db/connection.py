from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os 


url = os.environ.get('URL') 
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
base = declarative_base()

def connection():
    try:
        if(engine):
            print("yoyoyoyo")
    except Exception as e:
        print(e)