from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from itsdangerous import URLSafeTimedSerializer
from app.models import User, File
from app.dependencies import get_db, role_required
from app.config import settings

router = APIRouter()

serializer = URLSafeTimedSerializer(settings.SECRET_KEY)


# download link Endpoint
@router.get("/download-file/{assignment_id}")
def generate_download_link(
    assignment_id: int,
    db: Session = Depends(get_db),
    user = Depends(role_required("Client"))
):
    file = db.query(File).filter(File.id == assignment_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    
    token = serializer.dumps({"file_id": assignment_id, "user_id": user.id})
    download_url = f"/client/secure-download/{token}"
    return {"download-link": download_url, "message": "success"}




#doewmload Endpoint
@router.get("/secure-download/{token}")
def secure_download(
    token: str,
    db: Session = Depends(get_db),
    user = Depends(role_required("Client"))
):
    try:
        data = serializer.loads(token, max_age=3600)
        file_id = data["file_id"]
        user_id = data["user_id"]

        if user_id != user.id:
            raise HTTPException(status_code=403, detail="Access denied")

        file = db.query(File).filter(File.id == file_id).first()
        if not file:
            raise HTTPException(status_code=404, detail="File not found")

        file_path = f"{settings.UPLOAD_FOLDER}/{file.filename}"
        return FileResponse(file_path, media_type="application/octet-stream", filename=file.filename)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid or expired link")
