from fastapi import APIRouter

router = APIRouter(tags=["schedule"])

@router.get("/fieldboss")
def fieldboss():
    return {"ok": True, "message": "fieldboss endpoint ready", "data": []}

@router.get("/chaosgate")
def chaosgate():
    return {"ok": True, "message": "chaosgate endpoint ready", "data": []}

@router.get("/adventure")
def adventure():
    return {"ok": True, "message": "adventure island endpoint ready", "data": []}
