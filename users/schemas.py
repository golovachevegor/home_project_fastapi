from pydantic import BaseModel, EmailStr, Field
from typing import Annotated
from annotated_types import MinLen, MaxLen


class CreateUser(BaseModel):
    user_name: str = Field(..., min_length=3, max_length=20)
    # user_name: str = Annotated[str, MinLen(5), MaxLen(20)]
    users_email: EmailStr
