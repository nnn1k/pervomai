from backend.src.modules.users.exc import incorrect_login_or_password_exc
from backend.src.modules.users.repository import UserRepository
from backend.src.modules.users.schemas import UserSchema, LoginForm

from fastapi import Response

from backend.src.utils import jwt_token


class UserService:

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_user(self, **kwargs) -> UserSchema:
        user = await self.user_repo.get_user(**kwargs)
        schema = UserSchema.model_validate(user)
        return schema

    async def login(self, login_form: LoginForm, response: Response) -> UserSchema:
        user = await self.user_repo.login(login=login_form.login, password=login_form.password)
        if not user:
            raise incorrect_login_or_password_exc
        schema = UserSchema.model_validate(user)
        self.create_token(response=response, user=schema)
        return schema

    async def logout(self, response: Response) -> None:
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

    @staticmethod
    def create_token(response: Response, user: UserSchema) -> None:
        access_token = jwt_token.create_access_token(payload={'id': user.id})
        refresh_token = jwt_token.create_refresh_token(payload={'id': user.id})

        response.set_cookie('access_token', access_token, max_age=60 * 60 * 24 * 365)
        response.set_cookie('refresh_token', refresh_token, max_age=60 * 60 * 24 * 365)