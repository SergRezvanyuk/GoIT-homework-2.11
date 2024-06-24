from fastapi import FastAPI
from routers import contacts
from dependencies.database import engine, Base

# Створення таблиць
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Підключення роутера
app.include_router(contacts.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Contact Management API"}
