from sqlalchemy import Column, Integer, String
from .db import Base

class warns(Base):

    __tablename__ = 'warns'

    id = Column(Integer, primary_key=True, index=True,  unique=True)
    User = Column(String)
    Duration = Column(String)
    Reason = Column(String)
    given = Column(Integer)
    author = Column(String)


class black(Base):

    __tablename__ = 'black'

    user = Column(Integer, primary_key=True)
    reason = Column(String)
    duration = Column(Integer)
    author = Column(Integer)
    given = Column(Integer)
    
class ticket(Base):

    __tablename__ = 'ticket'

    id = Column(Integer, primary_key=True, index=True,  unique=True)
    channel = Column(Integer)
    user = Column(Integer)
    date = Column(Integer)
    
class ticket_rep(Base):

    __tablename__ = 'ticket_rep'

    id = Column(Integer, primary_key=True, index=True,  unique=True)
    channel = Column(Integer)
    user = Column(Integer)
    date = Column(Integer)

class ticket_bug(Base):

    __tablename__ = 'ticket_bug'

    id = Column(Integer, primary_key=True, index=True,  unique=True)
    channel = Column(Integer)
    user = Column(Integer)
    date = Column(Integer)
    
class donat(Base):

    __tablename__ = 'donat'

    id = Column(Integer, primary_key=True, index=True,  unique=True)
    user = Column(String)
    price = Column(Integer)
    price_text = Column(String)
    date = Column(String)