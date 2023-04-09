import time
import aiofiles
from fake import tts
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    # "http://localhost:8080",
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/fake_download")
async def fake_download(text:str,voice:str):
    time.sleep(1)
    tts(f"./voics/{voice}",text)
    return FileResponse("res.wav", media_type='application/octet-stream',filename="res.wav")

@app.post("/upload")
async def create_upload_file(file: UploadFile):
    async with aiofiles.open(f"./voics/temp.wav", 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write