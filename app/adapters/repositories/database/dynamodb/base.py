from app.core.interfaces.repositories.db import BaseDBRepository


class BaseDynamoDBRepository(BaseDBRepository):
    TABLE_NAME: str

    def create(self, data: dict) -> dict:
        ...

    def read(self, uid: str) -> dict:
        ...

    def read_all(self) -> list:
        ...

    def update(self, uid: str, data: dict) -> dict:
        ...

    def delete(self, uid: str) -> dict:
        ...
