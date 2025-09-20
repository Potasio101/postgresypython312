from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    userName = Column(String, unique=True, nullable=False)
    givenName = Column(String)
    familyName = Column(String)
    email = Column(String, unique=True)
    active = Column(Boolean, default=True)
