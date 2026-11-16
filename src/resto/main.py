from fastapi import FastAPI

from resto.api.health import router as health_router

app = FastAPI(
    title="Resto Assistant",
    description="Assistant IA de prise de commandes pour restaurants",
    version="0.1.0",
)

app.include_router(health_router)