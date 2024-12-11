import os

class Settings:
    SECRET_KEY = "ez_jwt_secret_key"
    DATABASE_URL = "sqlite:///./file_sharing.db"
    UPLOAD_FOLDER = "./app/uploads"

settings = Settings()
os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)
