from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    id: int
    login: str

    model_config = ConfigDict(from_attributes=True)


class LoginForm(BaseModel):
    login: str
    password: str

