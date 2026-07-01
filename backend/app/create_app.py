from fastapi import FastAPI

from app.api.routes import router


def create_app() -> FastAPI:
    """
    Creates and configures the HERMES application.
    """

    app = FastAPI(
        title="HERMES V1",
        description="Hybrid Evidence-driven Ranking with Modular Expert Systems",
        version="1.0.0",
    )

    app.include_router(router)

    return app