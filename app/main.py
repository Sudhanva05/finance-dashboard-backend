from fastapi import FastAPI
from app.routes import auth
from app.routes import test
from app.routes import records



app = FastAPI(
    title="Finance Dashboard Backend",
    description="Backend for finance records with role-based access control",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(test.router, prefix="/test", tags=["Test"]) 
app.include_router(records.router, prefix="/records", tags=["Records"])


@app.get("/")
def root():
    return {"message": "Finance API running "}