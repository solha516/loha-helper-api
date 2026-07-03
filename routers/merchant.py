from fastapi import APIRouter, Query
from services.merchant_service import get_merchants

router = APIRouter(prefix="/merchant", tags=["merchant"])

@router.get("")
def merchant(server: str | None = Query(default=None, description="Lost Ark server name, e.g. 카제로스")):
    return get_merchants(server=server)
