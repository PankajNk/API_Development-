from pydantic import BaseModel, EmailStr

# User
class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr

class UserLogin(BaseModel):
    username: str
    password: str

# File
class FileResponse(BaseModel):
    id: int
    filename: str

    class Config:
        orm_mode = True
