from typing import List, Dict, Any
from app.core.interfaces.services import (
    CustomerService as CustomerServiceInterface)
from app.core.models import Customer
from app.core.interfaces.repositories.db import CustomerDBRepository


class CustomerService(CustomerServiceInterface):
    def __init__(self, repository: CustomerDBRepository):
        self.repository = repository

    def create(self, data: Dict[str, Any]) -> Customer: ...

    def read(self, uid: str) -> Customer: ...

    def read_all(self) -> List[Customer]: ...

    def update(self, uid: str, data: Dict[str, Any]) -> Customer: ...

    def delete(self, uid: str) -> Customer: ...
