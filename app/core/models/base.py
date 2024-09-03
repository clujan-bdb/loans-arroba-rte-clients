from pydantic import BaseModel as PydanticBaseModel, ConfigDict, Field
from uuid import UUID, uuid4
from datetime import datetime


class BaseModel(PydanticBaseModel):
    uid: UUID = Field(default_factory=lambda: uuid4())
    active: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    model_config = ConfigDict(
        arbitrary_types_allowed=True, from_attributes=True)
