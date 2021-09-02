from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

@app.post("/files/")
async def create_file(files: List[bytes] = File(...)):
    contentReceived = []

    for file in files:
        contentReceived.append(str(file))

    return {"contentReceived": contentReceived}

@app.post("/uploadfiles/")
async def create_upload_file(files:List[UploadFile] = File(...)):
    fileNames = []

    for file in files:
        fileNames.append(file.filename)

    return {"fileNames": fileNames}