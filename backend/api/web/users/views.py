from typing import List

from pydantic import BaseModel

from api.web.networks.views import NetworkView


class UserView(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    networks: List[NetworkView] = []

    class Config:
        from_attributes = True


class CreateUserPayloadView(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str


class LoginPayloadView(BaseModel):
    email: str
    password: str
