from fastapi import APIRouter, Depends
from app.core.security import require_role

router = APIRouter()

@router.get("/admin-only")
def admin_only(user=Depends(require_role(["admin"]))):
    return {"message": "Welcome Admin"}