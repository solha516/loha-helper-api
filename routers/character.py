import os
import httpx
from fastapi import APIRouter, HTTPException, Query

router = APIRouter(prefix="/character", tags=["character"])

@router.get("")
async def character(name: str = Query(...)):
    api_key = os.getenv("LOSTARK_API_KEY", "")
    if not api_key:
        return {"ok": False, "message": "LOSTARK_API_KEY is not set yet", "name": name}
    url = f"https://developer-lostark.game.onstove.com/armories/characters/{name}/profiles"
    headers = {"authorization": f"bearer {api_key}"}
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(url, headers=headers)
    if r.status_code >= 400:
        raise HTTPException(status_code=r.status_code, detail=r.text)
    return r.json()
