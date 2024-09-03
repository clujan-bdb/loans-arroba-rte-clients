from typing import Literal
from datetime import datetime
from pydantic import Field
from .base import BaseModel
from .value_objects import IdentificationType, Segment


class Customer(BaseModel):
    identification_type: Literal[*IdentificationType.all]
    identification_number: str
    name: str
    middle_name: str
    last_name: str
    second_last_name: str
    email: str
    birth_date: Field(default_factory=datetime.now)
    segment: Literal[*Segment.all]
