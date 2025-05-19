from fastapi import FastAPI, UploadFile, File
import shutil, os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/stats")
def stats():
    return {"processed_files": len(os.listdir("watch_dir/processed/"))}

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    file_location = f"watch_dir/unprocessed/{file.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"info": f"file '{file.filename}' saved"}

@app.get("/files")
def list_files():
    return {"files": os.listdir("watch_dir/processed/")}
