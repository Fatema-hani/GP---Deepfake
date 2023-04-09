import time
from fastapi import FastAPI, Response, File, UploadFile
from fake import fake_it
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import aiofiles


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
def download_it_named(vid:str="3.mp4" ,img:str= "00.png" ,config="vox-adv"):
    time.sleep( 1 )
    driving_video=f"videos/{vid}"
    source_image=f"images/{img}"
    res=fake_it(driving_video=driving_video,source_image=source_image ,config="config/vox-adv-256.yaml",checkpoint="vox-adv-cpk.pth.tar")
    return FileResponse("result.mp4", media_type='application/octet-stream',filename="res.mp4")
 
@app.get("/download_last")
def download_last(vid:str="result.mp4"):
    return FileResponse("result.mp4", media_type='application/octet-stream',filename="res.mp4")


# @app.post("/files")
# async def create_file(file: bytes = File()):
#     return {"file_size": len(file)}


# @app.get("/uploadfile")
# async def create_upload_file(file: UploadFile, vid:str="3.mp4",config="vox-adv"):
#     async with aiofiles.open(f"./images/temp.jpg", 'wb') as out_file:
#         content = await file.read()  # async read
#         await out_file.write(content)  # async write
#     driving_video=f"videos/{vid}"
#     source_image=f"images/temp.jpg"
#     res=fake_it(driving_video=driving_video,source_image=source_image ,config="config/vox-adv-256.yaml",checkpoint="vox-adv-cpk.pth.tar")
#     return FileResponse("result.mp4", media_type='application/octet-stream',filename="res.mp4")
 
    
@app.post("/upload")
async def create_upload_file(file: UploadFile):
    async with aiofiles.open(f"./images/temp.jpg", 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write
