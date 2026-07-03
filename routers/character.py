from fastapi import APIRouter, Query

router = APIRouter(prefix="/character", tags=["character"])

@router.get("")
def character(name: str | None = Query(default=None)):
    return {
        "status": "ready",
        "message": "Lost Ark Open API 연결 준비 endpoint입니다.",
        "name": name,
    }
