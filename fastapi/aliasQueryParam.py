from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

@app.get("/emps")
def empsInfo(
    ids : List[int] = Query(
        [2, 3], 
        alias='emp-id', 
        description="Please provide valid employee ids"
    )
):
    return {"ids" : ids}
    