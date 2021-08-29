from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/products/{productId}/{noOfItems}/{infoLevel}/{formatType}")
def productInfo(
    infoLevel : str,
    productId: str = Path(
        ...,
        min_length = 4, 
        max_length=50,  
        title='Product id',
        description = "Enter valid product id"
        ), 
    noOfItems : int = Path(..., gt = 0, lt = 50, title='Number of items to return'),
    formatType : str = Path(..., min_length=2)
):
    return {"productId" : productId, "noOfItems" : noOfItems, 'infoLevel' : infoLevel, 'formatType' : formatType}

@app.get("/products/by-email/{email}")
def productsbyEmail(
    email: str = Path(..., max_length=50,  title='Valid email id', regex='[^@]+@[^@]+\.[^@]+')
):
    return {"email" : email}

