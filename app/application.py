from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import UJSONResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from app.web.router import api_router
from app.web import monitor
from app.middleware import profiler
from app.helper.response_helper import BaseResponse
from app.lifetime import register_startup_event, register_shutdown_event
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import logging.config

APP_ROOT = Path(__file__).parent.parent
logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="boilerplate app",
        description="this is fastapi boilerplate demo project",
        version="1.0",
        docs_url=None,
        redoc_url=None,
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Custom request exception handler
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return BaseResponse.request_exception_response(exc)

    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    # Add middleware
    app.add_middleware(middleware_class=profiler.ProfilerMiddleware)

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")
    app.include_router(router=monitor.router)

    # Adds static directory.
    # This directory is used to access swagger files.
    app.mount(
        "/static",
        StaticFiles(directory=APP_ROOT / "static"),
        name="static"
    )

    return app
