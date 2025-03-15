# routers.py

from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()

# Set up templates
templates = Jinja2Templates(directory="templates")

# Ensure the uploads directory exists
UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# In-memory storage for the uploaded filename
user_profile = {"filename": "default.png"}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # Update the user profile with the new filename
    user_profile["filename"] = file.filename
    return {"filename": file.filename}

@router.get("/profile", response_class=HTMLResponse)
async def get_profile(request: Request):
    # Pass the filename to the template
    return templates.TemplateResponse("profile.html", {"request": request, "filename": user_profile["filename"]})