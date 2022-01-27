'''
Created on 2022年1月18日

@author: Ning_Lin
'''
from fastapi import FastAPI
import schemas, models

app = FastAPI()
@app.post('/record')
def health_tracking(item: schemas.Item):
    return item