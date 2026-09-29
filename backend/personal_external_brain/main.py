from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from personal_external_brain.api import router
from personal_external_brain.config import settings
from personal_external_brain.workspace import get_workspace


@asynccontextmanager
async def lifespan(_app: FastAPI):
    workspace = get_workspace()
    try:
        yield
    finally:
        workspace.graph.close()


app = FastAPI(title="Personal External Brain", version="0.1.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
