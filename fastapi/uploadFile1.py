from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file), "data_received" : str(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    content = file.file.read()
    return {"filename": file.filename, "data_received": content}