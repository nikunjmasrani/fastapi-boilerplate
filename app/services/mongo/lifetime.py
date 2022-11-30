from fastapi import FastAPI
from app.settings import settings
from motor import motor_asyncio


def init_mongo(app: FastAPI) -> None:  # pragma: no cover
    """
    Creates connection pool for Mong.

    :param app: current fastapi application.
    """

    app.state.mongo_client = motor_asyncio.AsyncIOMotorClient(str(settings.mongo_url))


async def shutdown_mongo(app: FastAPI) -> None:  # pragma: no cover
    """
    Closes mongo connection.

    :param app: current FastAPI app.
    """
    app.state.mongo_client.close()
