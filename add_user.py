from werkzeug.security import generate_password_hash
from app.database import SessionLocal
from app.models import User


db = SessionLocal()

# seeding the user to database 
# Add Ops User
ops_user = User(
    username="opsuser",
    password=generate_password_hash("opspassword"),
    email="opsuser@example.com",
    role="Ops",
    email_verified=True  
)

# Add Client User
client_user = User(
    username="clientuser",
    password=generate_password_hash("clientpassword"),
    email="clientuser@example.com",
    role="Client",
    email_verified=True
)


db.add(ops_user)
db.add(client_user)


db.commit()
db.close()

print("Users added successfully!")
