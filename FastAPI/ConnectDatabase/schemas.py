'''
Created on 2022年1月18日

@author: Ning_Lin
'''
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    date:str
    systolic_pressure:int
    diastolic_pressure:int
    heart_beat:int
    period:str
    degree:Optional[int]