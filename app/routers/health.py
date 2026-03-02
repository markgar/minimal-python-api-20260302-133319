import logging
from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/health")
def get_health() -> dict:
    return {"status": "healthy"}
