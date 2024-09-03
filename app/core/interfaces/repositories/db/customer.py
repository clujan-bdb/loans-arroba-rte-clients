from abc import ABC
from .base import BaseDBRepository
from app.core.models.customer import Customer


class CustomerDBRepository(ABC, BaseDBRepository):
    MODEL = Customer
