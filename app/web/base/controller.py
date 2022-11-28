from abc import ABC, abstractmethod
from typing import Any


class BaseService(ABC):

    @abstractmethod
    async def create(self, data: Any, *args, **kwargs):
        pass

    @abstractmethod
    async def get(self, data: Any, *args, **kwargs):
        pass

    @abstractmethod
    async def delete(self, data: Any, *args, **kwargs):
        pass

    @abstractmethod
    async def get_list(self, data: Any, *args, **kwargs):
        pass

    @abstractmethod
    async def update(self, data: Any, *args, **kwargs):
        pass
