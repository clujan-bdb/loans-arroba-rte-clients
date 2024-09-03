from .base import BaseDynamoDBRepository


class CustomerDynamoDBRepository(BaseDynamoDBRepository):
    TABLE_NAME = "customer"
