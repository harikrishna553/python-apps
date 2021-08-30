from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/products")
def productInfo(
    infoLevel : str,
    formatType : str = Query('JSON', min_length=2, deprecated=True),
    productId: str = Query(
        ...,
        min_length = 4, 
        max_length=50,  
        title='Product id',
        description = "Enter valid product id"
        ), 
    noOfItems : Optional[int] = Query(None, gt = 0, lt = 50, title='Number of items to return')
):
    return {
        'productId' : productId, 
        'noOfItems' : noOfItems, 
        'infoLevel' : infoLevel, 
        'formatType' : formatType
    }
