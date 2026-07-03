from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import merchant, lostark

app = FastAPI(
    title="LoHA Helper API",
    version="0.1.0",
    description="API server for LoA Helper web/program",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(merchant.router)
app.include_router(lostark.router)


@app.get("/")
def root():
    return {
        "name": "LoHA Helper API",
        "status": "ok",
        "docs": "/docs",
        "endpoints": [
            "/merchant",
            "/merchant?server=카제로스",
            "/fieldboss",
            "/chaosgate",
            "/adventure",
            "/character/{name}",
        ],
    }


@app.get("/health")
def health():
    return {"ok": True}
