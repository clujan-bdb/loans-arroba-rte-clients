from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Dict, Any
from .base import BaseService
from app.core.interfaces.repositories.db import CustomerDBRepository
from app.core.models import Customer


class CustomerService(ABC, BaseService):
    @abstractmethod
    def __init__(self, repository: CustomerDBRepository):
        self.repository = repository

    @abstractmethod
    def create(self, data: Dict[str, Any]) -> Customer: ...

    @abstractmethod
    def read(self, uid: UUID) -> Customer: ...

    @abstractmethod
    def read_all(self) -> List[Customer]: ...

    @abstractmethod
    def update(self, uid: UUID, data: Dict[str, Any]) -> Customer: ...

    @abstractmethod
    def delete(self, uid: UUID) -> Customer: ...
