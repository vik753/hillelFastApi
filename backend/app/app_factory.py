import socket
from fastapi import FastAPI
from settings import settings


def get_application() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        root_path="/api",
    )

    @app.get("/info")
    async def get_backend():
        1 / 0
        return {"backend": socket.gethostname()}

    return app
