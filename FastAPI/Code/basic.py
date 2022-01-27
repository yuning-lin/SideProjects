'''
Created on 2022年1月14日

@author: Ning_Lin
'''
'''
若要在 eclipse debug，可以使用 if __name__=='__main__':配合下中斷點來執行
若是有同樣的 port 被執行，需先結束後才可以 debug
或是指定在別的 port 上執行 debug mode
CMD: unicorn Code.basic:app --reload
'''
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name:str
    date:str
    systolic_pressure:int
    diastolic_pressure:int
    heart_beat:int
    period:str
    degree:Optional[int]

@app.post('/')
def health_tracking(item: Item):
    return {'data':{f"{item.name}\'s health tracking data"}}

if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)
