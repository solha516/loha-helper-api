from fastapi import APIRouter, Query
from services.merchant_service import get_merchants

router = APIRouter(tags=["merchant"])


@router.get("/merchant")
async def merchant(server: str | None = Query(default=None, description="예: 카제로스")):
    return await get_merchants(server=server)
