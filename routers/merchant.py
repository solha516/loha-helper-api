from fastapi import APIRouter, Query
from services.merchant_service import get_merchants

router = APIRouter(prefix="/merchant", tags=["merchant"])

@router.get("")
def merchant(server: str | None = Query(default=None)):
    return get_merchants(server)
