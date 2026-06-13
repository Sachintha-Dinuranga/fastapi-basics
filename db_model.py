
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# declare base
Base = declarative_base()

# sql alchemy model
class Product(Base):

    #declare table name
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name =  Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
