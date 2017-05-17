from sqlalchemy import (
	Integer,
    Column,
    DateTime,
    ForeignKey,
    Text,
    Unicode,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

from .meta import Base

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

class Customer(Base):
    """Declarative model class for Customer object. """
    __tablename__ = 'customer'
    
    id = Column('customer_id', Integer, primary_key=True) 
    company_name = Column(Unicode(100), nullable=False, unique=True)
    # foreing key
    # nullable = false, the customer must have a category
    category_id = Column(Integer, ForeignKey('category.category_id',
        name="fk_customer_category", onupdate='CASCADE', ondelete='RESTRICT'), nullable=False)
    category = relationship("Category", passive_updates=True)
    contact_title = Column(Unicode(50))
    contact_first_name = Column(Unicode(50))
    contact_last_name = Column(Unicode(50))
    address = Column(Text)
    city = Column(Unicode(50))
    region = Column(Unicode(50))
    postal_code = Column(Unicode(50))
    # foreing key, nullable =  true 
    country_id = Column(Integer, ForeignKey('country.country_id',
        name='fk_customer_country', onupdate='CASCADE', ondelete='RESTRICT'), nullable=True)
    country = relationship("Country", passive_updates=True)
    mobile = Column(Unicode(50))
    email = Column(Unicode(50))
    notes = Column(Text)
    created_by_user = Column(Unicode(50))  
    created_at = Column(DateTime)  
    updated_by_user = Column(Unicode(50))  
    updated_at = Column(DateTime)