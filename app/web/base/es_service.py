from abc import ABC, abstractmethod
from typing import Any, Dict, List


class ESService(ABC):

    @abstractmethod
    async def index_data(self, data: Any, *args, **kwargs) -> None:
        pass

    @abstractmethod
    async def reindex_data(self, _id: Any, *args, **kwargs) -> None:
        pass

    @abstractmethod
    async def query_data(self, data: Any, *args, **kwargs) -> List[Dict]:
        pass

    @abstractmethod
    async def delete_data(self, data: Any, *args, **kwargs) -> None:
        pass




