from datetime import datetime
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field


class UserCreate(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Unique username"
    )

    email: EmailStr

    first_name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    last_name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    role: Literal["admin", "user", "guest"]


class UserUpdate(BaseModel):
    username: Optional[str] = Field(
        None,
        min_length=3,
        max_length=50
    )

    email: Optional[EmailStr] = None

    first_name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=100
    )

    last_name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=100
    )

    role: Optional[Literal["admin", "user", "guest"]] = None

    active: Optional[bool] = None


class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    role: str
    active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)