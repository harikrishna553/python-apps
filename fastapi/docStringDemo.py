from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get(
    "/emps", 
    tags=["employees"], 
    summary="Get employees"
)
def emps():
    """
        This api is used to return all the active employees from database.models

        - **id** -> Represent user id
        - **name** -> Represent user name
    """

    return {"msg": "Return all employees"}