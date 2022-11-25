import uuid
from app.settings import settings
from datetime import datetime
from elasticsearch import AsyncElasticsearch


class Profile:

    def __init__(self, es_client: AsyncElasticsearch):
        self.es_client = es_client

    async def index_user(self, data):
        doc = {
            'name': data.name,
            'about': data.about,
            'created_at': str(datetime.now())
        }
        es_user_result = await self.es_client.create(index=settings.es_user_index,
                                                     id=str(uuid.uuid4()),
                                                     document=doc)

