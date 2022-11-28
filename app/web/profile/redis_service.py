from typing import Any, Dict

from redis.asyncio import ConnectionPool, Redis
from app.web.base.redis_service import RedisService
import json


class Profile(RedisService):
    def __init__(self, redis_pool: ConnectionPool):
        self.redis_pool = redis_pool

    async def set_data(self, data: Any, *args, **kwargs) -> None:
        """
        function set user data obj in redis.
        :param data:
        :param args:
        :param kwargs:
        :return None:
        """
        async with Redis(connection_pool=self.redis_pool) as redis:
            doc = {
                "name": data.get("name"),
                "about": data.get("about")
            }
            await redis.set(data.get('id'), json.dumps(doc))

    async def get_data(self, _id: Any, *args, **kwargs) -> Dict:
        """
        function returns user data from redis
        :param _id:
        :param args:
        :param kwargs:
        :return Dict:
        """
        pass





