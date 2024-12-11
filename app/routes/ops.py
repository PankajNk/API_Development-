from fastapi import APIRouter, Depends, UploadFile, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.dependencies import get_db, role_required
from app.auth import create_access_token
from app.models import File, User
from app.config import settings
from werkzeug.security import check_password_hash

router = APIRouter()



# Upload file endpoint
@router.post("/upload")
def upload_file(
    file: UploadFile,
    db: Session = Depends(get_db),
    user=Depends(role_required("Ops"))
):
    allowed_extensions = ["pptx", "docx", "xlsx"]
    if file.filename.split(".")[-1] not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Invalid file type")

    filepath = f"{settings.UPLOAD_FOLDER}/{file.filename}"
    with open(filepath, "wb") as f:
        f.write(file.file.read())

    new_file = File(filename=file.filename, uploaded_by=user.id)
    db.add(new_file)
    db.commit()
    return {"msg": "File uploaded successfully"}




# Login endpoint
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    print(f"Login attempt for username: {form_data.username}")  
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user:
        print(f"User not found: {form_data.username}")  # Debug log
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not check_password_hash(user.password, form_data.password):
        print(f"Password mismatch for username: {form_data.username}")  # Debug log
        raise HTTPException(status_code=401, detail="Invalid credentials")

    print(f"Login successful for username: {user.username}")  # Debug log
    token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

