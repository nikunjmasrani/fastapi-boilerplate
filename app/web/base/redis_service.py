from abc import ABC, abstractmethod
from typing import Any, Dict


class RedisService(ABC):

    @abstractmethod
    async def set_data(self, data: Any, *args, **kwargs) -> None:
        pass

    @abstractmethod
    async def get_data(self, _id: Any, *args, **kwargs) -> Dict:
        pass

