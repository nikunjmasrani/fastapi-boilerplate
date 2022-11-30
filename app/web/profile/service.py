from app.web.base.service import BaseService
from app.web.profile.db_service import Profile as ProfileDBService
from app.web.profile.es_service import Profile as ProfileESService
from app.web.profile.mongo_service import Profile as ProfileMongoService
from app.web.profile.redis_service import Profile as ProfileRedisService
from typing import Any, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from elasticsearch import AsyncElasticsearch
from motor.motor_asyncio import AsyncIOMotorClient
from redis.asyncio import ConnectionPool


class Profile(BaseService):
    def __init__(
        self,
        db_session: AsyncSession = None,
        es_client: AsyncElasticsearch = None,
        redis_pool: ConnectionPool = None,
        mongo_client: AsyncIOMotorClient = None,
    ):
        self.db_session = db_session
        self.es_client = es_client
        self.redis_pool = redis_pool
        self.mongo_client = mongo_client

    async def create(self, data: Any, *args, **kwargs) -> Dict:
        """
        function to store user data in DB, indexes data in ES and set data in Redis
        :param data:
        :param args:
        :param kwargs:
        :return Dict:
        """
        profile_db_service = ProfileDBService(self.db_session)
        profile_es_service = ProfileESService(self.es_client)
        profile_redis_service = ProfileRedisService(self.redis_pool)
        profile_mongo_service = ProfileMongoService(self.mongo_client)
        user = await profile_db_service.insert_data(data)
        await profile_es_service.index_data(data)
        await profile_redis_service.set_data(user)
        saved_user_id = await profile_mongo_service.insert_data(user)
        user["mongo_user_id"] = saved_user_id

        return user

    async def get(self, data: Any, *args, **kwargs) -> Dict:
        """
        functon returns user data from DB
        :param data:
        :param args:
        :param kwargs:
        :return Dict:
        """
        profile_service = ProfileDBService(self.db_session)
        user = await profile_service.get_data_by_id(data)
        return user

    async def delete(self, data: Any, *args, **kwargs):
        """
        function to delete user from system
        :param data:
        :param args:
        :param kwargs:
        :return:
        """

    async def update(self, data: Any, *args, **kwargs):
        """
        function to update user.
        :param data:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    async def get_list(self, data: Any, *args, **kwargs):
        """
        function to get list of all users
        :param data:
        :param args:
        :param kwargs:
        :return:
        """
