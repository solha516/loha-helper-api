from fastapi import APIRouter

router = APIRouter(prefix="/schedules", tags=["schedules"])

@router.get("/fieldboss")
def fieldboss():
    return {"status": "ready", "type": "fieldboss", "items": []}

@router.get("/chaosgate")
def chaosgate():
    return {"status": "ready", "type": "chaosgate", "items": []}

@router.get("/adventure")
def adventure():
    return {"status": "ready", "type": "adventure", "items": []}
