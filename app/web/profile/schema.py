from app.services.db.base import Base
from sqlalchemy import Column, Integer, String, Boolean

class User(Base):
   __tablename__ = "user"
   id = Column(Integer, primary_key=True)
   name = Column(String)
   about = Column(String)
   is_public = Column(Boolean)
