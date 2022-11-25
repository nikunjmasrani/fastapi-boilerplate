from typing import AsyncGenerator
from elasticsearch import AsyncElasticsearch
from starlette.requests import Request


async def get_es_client(request: Request) -> AsyncGenerator[AsyncElasticsearch, None]:  # pragma: no cover
    """
    Returns elasticsearch client.
    """
    return request.app.state.es_client
