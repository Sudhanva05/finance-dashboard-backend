from fastapi import FastAPI

app = FastAPI(
    title="Finance Dashboard Backend",
    description="Backend for finance records with role-based access control",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Finance API running 🚀"}