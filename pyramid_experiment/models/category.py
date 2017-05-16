from sqlalchemy import (
	Integer,
    Column,
    DateTime,
    Unicode,
)

from .meta import Base


class Category(Base):
    """ Declarative model class for Category object. """
    __tablename__ = 'category'
    
    id = Column('category_id', Integer, primary_key=True) 
    name = Column(Unicode(100), nullable=False, unique=True)
    created_by_user = Column(Unicode(50))  
    created_at = Column(DateTime)  
    updated_by_user = Column(Unicode(50))  
    updated_at = Column(DateTime)