from typing import Any, Dict
from app import constants
from app.web.base.mong_service import MongoService
from motor.motor_asyncio import AsyncIOMotorClient


class Profile(MongoService):
    def __init__(self, mongo_client: AsyncIOMotorClient):
        self.mongo_client = mongo_client

    async def insert_data(self, data: Any, *args, **kwargs) -> str:
        """
        function to insert user data to MongoDB
        :param data:
        :param args:
        :param kwargs:
        :return:
        """

        user_data = {
            "name": data.get("name"),
            "about": data.get("about"),
            "is_public": data.get("public"),
        }
        saved_user = await self.mongo_client[constants.USER_DB][
            constants.USER_COLLECTIONS
        ].insert_one(user_data)
        return str(saved_user.inserted_id)

    async def get_data(self, _id: Any, *args, **kwargs) -> Dict:
        """
        function to get user data from MongoDB
        :param _id:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    async def delete_data(self, _id: Any, *args, **kwargs) -> Dict:
        """
        function to delete user data from MongoDB
        :param _id:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    async def update_data(self, _id: Any, *args, **kwargs) -> Dict:
        """
        function to update user data into MongoDB
        :param _id:
        :param args:
        :param kwargs:
        :return:
        """
