
from fastapi import  APIRouter

router = APIRouter(
    prefix="/health"
)

@router.get("")
def health():
    return {"status": "ok",
            "app": "task-processor",
            "version": "0.1.0" }