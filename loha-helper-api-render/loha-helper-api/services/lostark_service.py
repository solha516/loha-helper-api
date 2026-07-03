import os
import httpx

LOSTARK_API_BASE = "https://developer-lostark.game.onstove.com"


def _headers():
    key = os.getenv("LOSTARK_API_KEY", "").strip()
    if not key:
        return None
    return {"authorization": f"bearer {key}", "accept": "application/json"}


async def get_character(name: str):
    headers = _headers()
    if not headers:
        return None

    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.get(f"{LOSTARK_API_BASE}/characters/{name}/siblings", headers=headers)
        if r.status_code >= 400:
            return None
        return {"character": name, "siblings": r.json()}


async def get_fieldboss():
    return {"status": "ready", "message": "필드보스 API 연결 예정"}


async def get_chaosgate():
    return {"status": "ready", "message": "카오스게이트 API 연결 예정"}


async def get_adventure():
    return {"status": "ready", "message": "모험섬 API 연결 예정"}
