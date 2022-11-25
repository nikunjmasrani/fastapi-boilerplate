from fastapi import FastAPI
from app.settings import settings
from elasticsearch import AsyncElasticsearch


def init_es(app: FastAPI) -> None:  # pragma: no cover
    """
    Creates connection pool for redis.

    :param app: current fastapi application.
    """

    app.state.es_client = AsyncElasticsearch(
        hosts=settings.es_host_url,
        basic_auth=(settings.es_user, settings.es_pass)
    )


async def shutdown_es(app: FastAPI) -> None:  # pragma: no cover
    """
    Closes redis connection pool.

    :param app: current FastAPI app.
    """
    await app.state.es_client.close()
