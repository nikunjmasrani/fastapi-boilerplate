from redis.asyncio import ConnectionPool, Redis
import json


class Profile:
    def __init__(self, redis_pool: ConnectionPool):
        self.redis_pool = redis_pool

    async def save_user(self,data):
        async with Redis(connection_pool=self.redis_pool) as redis:
            doc = {
                "name": data.get("name"),
                "about": data.get("about")
            }
            await redis.set(data.get('id'), json.dumps(doc))

