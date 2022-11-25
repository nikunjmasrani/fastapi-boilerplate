from app.web.base.controller import BaseController
from app.web.profile.db_service import Profile as ProfileDBService
from app.web.profile.es_service import Profile as ProfileESService
from app.web.profile.redis_service import Profile as ProfileRedisService
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from elasticsearch import AsyncElasticsearch
from redis.asyncio import ConnectionPool


class Profile(BaseController):

    def __init__(self, db_session: AsyncSession,
                 es_client: AsyncElasticsearch,
                 redis_pool: ConnectionPool):
        self.db_session = db_session
        self.es_client = es_client
        self.redis_pool = redis_pool

    async def create(self, data: Any, *args, **kwargs):
        profile_db_service = ProfileDBService(self.db_session)
        profile_es_service = ProfileESService(self.es_client)
        profile_redis_service = ProfileRedisService(self.redis_pool)
        user = await profile_db_service.create_profile(data)
        await profile_es_service.index_user(data)
        await profile_redis_service.save_user(user)
        return user

    async def get(self, data: Any, *args, **kwargs):
        profile_service = ProfileDBService(self.db_session)
        user = await profile_service.get_profile(data)
        return user

    async def delete(self, data: Any, *args, **kwargs):
        pass

    async def update(self, data: Any, *args, **kwargs):
        pass

    async def get_list(self, data: Any, *args, **kwargs):
        pass

