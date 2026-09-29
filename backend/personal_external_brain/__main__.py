import uvicorn

from personal_external_brain.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "personal_external_brain.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.should_reload(),
    )
