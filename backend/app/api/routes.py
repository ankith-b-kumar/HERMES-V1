from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Welcome to HERMES V1"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "HERMES V1"
    }