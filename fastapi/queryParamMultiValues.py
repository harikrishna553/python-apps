from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()

@app.get("/emps")
def empsInfo(
    ids : Optional[List[int]] = Query(None),
):
    return {"ids" : ids}
    