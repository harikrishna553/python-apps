from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
def home():
    return {'name' : 'Hello World app', 'version': '2.0.0'}

@app.get("/emps")
def emps(pageNum : int = 1, pageSize : int = 10):
    return {'received' : {'pageNum' : pageNum, 'pageSize': pageSize}}