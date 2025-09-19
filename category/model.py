from sqlalchemy import Column, Integer, String

from db import Base


class Category(Base):
    __tablename__ = "categories"

    id: int = Column(Integer, primary_key=True, index=True)
    code: str = Column(String, nullable=False, unique=True, index=True)
    name: str = Column(String)
