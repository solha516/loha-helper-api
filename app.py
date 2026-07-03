from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import merchant, character, schedules

app = FastAPI(
    title="LoA Helper API",
    description="Backend API for LoA Helper web and desktop app.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(merchant.router)
app.include_router(character.router)
app.include_router(schedules.router)

@app.get("/")
def root():
    return {
        "name": "LoA Helper API",
        "version": "1.0.0",
        "status": "ok",
        "endpoints": ["/health", "/merchant", "/merchant?server=카제로스", "/docs"],
    }

@app.get("/health")
def health():
    return {"status": "ok"}
