from fastapi import APIRouter, HTTPException
from services.lostark_service import get_character, get_fieldboss, get_chaosgate, get_adventure

router = APIRouter(tags=["lostark"])


@router.get("/character/{name}")
async def character(name: str):
    result = await get_character(name)
    if result is None:
        raise HTTPException(status_code=404, detail="character not found or LOSTARK_API_KEY is missing")
    return result


@router.get("/fieldboss")
async def fieldboss():
    return await get_fieldboss()


@router.get("/chaosgate")
async def chaosgate():
    return await get_chaosgate()


@router.get("/adventure")
async def adventure():
    return await get_adventure()
