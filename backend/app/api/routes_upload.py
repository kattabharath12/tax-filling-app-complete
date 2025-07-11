from fastapi import APIRouter, File, UploadFile, HTTPException
import os
import shutil
from app.ocr_mock import extract_fields_from_document

router = APIRouter()

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/document")
async def upload_document(file: UploadFile = File(...), doc_type: str = "W-2"):
    # Validate file type
    allowed_types = ["application/pdf", "image/jpeg", "image/png"]
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Save file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract data (mock)
    extracted_data = extract_fields_from_document(file_path, doc_type)

    return {
        "filename": file.filename,
        "doc_type": doc_type,
        "extracted_data": extracted_data,
        "status": "uploaded"
    }
