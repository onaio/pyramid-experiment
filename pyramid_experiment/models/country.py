from sqlalchemy import (
	Integer,
    Column,
    DateTime,
    Text,
    Unicode,
)

from .meta import Base


class Country(Base):  
    """ Declarative model class for Country object. """  
    __tablename__ = 'country'  
  
    id = Column('country_id', Integer, primary_key=True)  
    code = Column(Unicode(10), nullable=False, unique=True)  
    name = Column(Unicode(100), nullable=False, unique=True)
    created_by_user = Column(Unicode(50))  
    created_at = Column(DateTime)  
    updated_by_user = Column(Unicode(50))  
    updated_at = Column(DateTime)