from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Dict, Any
from app.core.models.base import BaseModel


class BaseDBRepository(ABC):
    MODEL: BaseModel

    @abstractmethod
    def create(self, data: Dict[str, Any]) -> BaseModel: ...

    @abstractmethod
    def read(self, uid: UUID) -> BaseModel: ...

    @abstractmethod
    def read_all(self) -> List[BaseModel]: ...

    @abstractmethod
    def update(self, uid: UUID, data: Dict[str, Any]) -> BaseModel: ...

    @abstractmethod
    def delete(self, uid: UUID) -> BaseModel: ...
