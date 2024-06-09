from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy import Column, Integer,Double, Sequence, String, Text, PrimaryKeyConstraint, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import and_
from datetime import datetime
from datetime import timedelta
from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()
connection_string = "mysql+pymysql://root:mechanix93@localhost/fastapi_mail_db"
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)

class EmailList(Base):
    __tablename__ = "email_list"
    id_email = Column(Integer)
    name_email = Column(String(70))
    __table_args__ = (PrimaryKeyConstraint(id_email), {},)

Base.metadata.create_all(engine)