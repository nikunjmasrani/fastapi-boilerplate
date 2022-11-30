from typing import AsyncGenerator
from starlette.requests import Request
from motor.motor_asyncio import AsyncIOMotorClient


async def get_mongo_client(
    request: Request,
) -> AsyncGenerator[AsyncIOMotorClient, None]:  # pragma: no cover
    """
    Returns elasticsearch client.
    """
    return request.app.state.mongo_client
