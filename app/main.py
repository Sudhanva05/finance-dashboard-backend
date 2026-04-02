from fastapi import FastAPI
from app.routes import auth

app = FastAPI(
    title="Finance Dashboard Backend",
    description="Backend for finance records with role-based access control",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
 

@app.get("/")
def root():
    return {"message": "Finance API running "}