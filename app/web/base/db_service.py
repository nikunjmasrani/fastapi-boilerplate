from abc import ABC, abstractmethod
from typing import Any, List, Dict


class DBService(ABC):

    @abstractmethod
    async def insert_data(self, data: Any, *args, **kwargs) -> Dict:
        pass

    @abstractmethod
    async def get_data_by_id(self, _id: Any, *args, **kwargs) -> Dict:
        pass

    @abstractmethod
    async def update_data(self, data: Any, *args, **kwargs) -> Dict:
        pass

    @abstractmethod
    async def delete_data(self, data: Any, *args, **kwargs) -> None:
        pass

    @abstractmethod
    async def get_all_data(self, data: Any, *args, **kwargs) -> List[Dict]:
        pass



