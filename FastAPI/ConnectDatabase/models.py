'''
Created on 2022年1月18日

@author: Ning_Lin
'''
from database import Base
from sqlalchemy import Column, DateTime, Integer, String
from datetime import datetime

class Record(Base):
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(DateTime, default=datetime.now)
    systolic_pressure = Column(Integer)
    diastolic_pressure = Column(Integer)
    heart_beat = Column(Integer)
    period = Column(String)
    degree = Column(Integer)