from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import merchant, schedules, character

app = FastAPI(title="LoA Helper API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"ok": True, "name": "LoA Helper API", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(merchant.router)
app.include_router(schedules.router)
app.include_router(character.router)
