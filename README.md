# Secure File Sharing System

This project is a secure file-sharing system built with FastAPI. It enables two types of users:
- **Ops Users**: Can upload files of specific types (e.g.. .docx, .xlsx, .pptx).
- **Client Users**: Can generate secure download links for files and download them securely.

## **Features**
- **User Authentication**:
  - Login with username and password using OAuth2 Password Flow.
  - Role-based access control (Ops User and Client User).
- **File Upload**:
  - Ops Users can upload files with strict type validation.
- **Secure File Downloads**:
  - Client Users can generate secure, tokenized download links.
  - Token-based file access ensures secure sharing.
- **Role-based Access**:
  - Different actions allowed for Ops and Client users.
- **Built-in Security**:
  - JWT-based authentication.
  - Token expiration and validation.

---

## **Tech Stack**
- **Backend**: FastAPI
- **Authentication**: OAuth2 with JWT
- **Database**: SQLite (can be extended to other relational databases)
- **Containerization**: Docker
- **Web Server**: Uvicorn

---

## **Installation**

### **1. Clone the Repository**
```bash
[git clone https://github.com/yourusername/secure-file-sharing.git](https://github.com/PankajNk/API_Development-.git)

