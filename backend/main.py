# backend/main.py

from fastapi import FastAPI

# Create a FastAPI app instance
app = FastAPI()

# Define your first API endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to Skill-Gap Minimiser Backend!"}

# You'll add more routers and services here as per your plan
# from .routers import auth, quiz, progress
# app.include_router(auth.router)
# app.include_router(quiz.router)
# app.include_router(progress.router)
