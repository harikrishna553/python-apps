from fastapi import FastAPI, File, UploadFile, Form
from typing import List

app = FastAPI()

@app.post("/upload")
def uploadData(files:List[UploadFile] = File(...),
                             msg : str = Form(...)):
    fileNames = []

    for file in files:
        fileNames.append(file.filename)

    return {"fileNames": fileNames, 'msg' : msg}