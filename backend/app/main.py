from fastapi import FastAPI
from app.modules.fleet.router import fleet_router

app = FastAPI(title="SIGI Backend")

app.include_router(fleet_router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
