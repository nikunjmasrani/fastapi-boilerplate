import uuid
from typing import Any, List, Dict

from app.settings import settings
from app.web.base.es_service import ESService
from datetime import datetime
from elasticsearch import AsyncElasticsearch


class Profile(ESService):

    def __init__(self, es_client: AsyncElasticsearch):
        self.es_client = es_client

    async def index_data(self, data: Any, *args, **kwargs) -> None:
        """
        function to index user data to es
        :param data:
        :param args:
        :param kwargs:
        :return None:
        """
        doc = {
            'name': data.name,
            'about': data.about,
            'created_at': str(datetime.now())
        }
        es_user_result = await self.es_client.create(index=settings.es_user_index,
                                                     id=str(uuid.uuid4()),
                                                     document=doc)

    async def reindex_data(self, _id: Any, *args, **kwargs) -> None:
        pass

    async def query_data(self, data: Any, *args, **kwargs) -> List[Dict]:
        pass

    async def delete_data(self, data: Any, *args, **kwargs) -> None:
        pass



