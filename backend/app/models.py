from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship

from database import Base


class Meme(Base):
    __tablename__ = "meme"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    caption = Column(String(80), nullable=False, unique=True)
    url = Column(String(80), nullable=False, unique=True)
    timestamp = Column(DateTime, nullable=False,
                       server_default=func.current_timestamp(), onupdate=func.current_timestamp())
