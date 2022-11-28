from typing import Any, List, Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import constants
from app.web.base.db_service import DBService
from app.web.profile.schema import User
from app.exception import CustomException


class Profile(DBService):

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def insert_data(self, data: Any, *args, **kwargs) -> Dict:
        """
        function to create user record in database and return dictionary
        :param data:
        :param args:
        :param kwargs:
        :return Dict:
        """
        select_query = select(User).where(User.name == data.name)
        existing_user_result = await self.db_session.execute(select_query)
        existing_user = list(existing_user_result.scalars())
        if existing_user:
            raise CustomException(message=constants.USER_ALREADY_EXISTS)
        user = User()
        user.name = data.name
        user.about = data.about
        user.is_public = data.is_public
        self.db_session.add(user)
        await self.db_session.commit()
        await self.db_session.refresh(user)
        return user.__dict__

    async def get_data_by_id(self, _id: Any, *args, **kwargs) -> Dict:
        """
        function to get single user by id
        :param _id:
        :param args:
        :param kwargs:
        :return Dict:
        """
        select_query = select(User).where(User.id == _id)
        user_result = await self.db_session.execute(select_query)
        user = list(user_result.scalars())
        if not user:
            raise CustomException(message=constants.USER_NOT_EXISTS)
        return user[0].__dict__

    async def update_data(self, data: Any, *args, **kwargs) -> Dict:
        pass

    async def delete_data(self, data: Any, *args, **kwargs) -> None:
        pass

    async def get_all_data(self, data: Any, *args, **kwargs) -> List[Dict]:
        pass
