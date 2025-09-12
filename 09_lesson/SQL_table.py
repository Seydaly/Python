from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"

    user_id = Column(Integer, primary_key=True, index=True)
    level = Column(String, nullable=False)
    education_form = Column(String, nullable=False)
    subject_id = Column(Integer, nullable=False)

DATABASE_URL = "ветка для подключения"
engine = create_engine(DATABASE_URL, future=True)

Base.metadata.create_all(bind=engine)
