from abc import ABC, abstractmethod
from typing import Any, Dict


class MongoService(ABC):
    @abstractmethod
    async def insert_data(self, data: Any, *args, **kwargs) -> None:
        pass

    @abstractmethod
    async def get_data(self, _id: Any, *args, **kwargs) -> Dict:
        pass

    @abstractmethod
    async def delete_data(self, _id: Any, *args, **kwargs) -> Dict:
        pass

    @abstractmethod
    async def update_data(self, _id: Any, *args, **kwargs) -> Dict:
        pass
