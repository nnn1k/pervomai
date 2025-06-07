from fastapi import APIRouter, Depends, Response

from backend.src.modules.users.dependencies import get_user_serv
from backend.src.modules.users.schemas import LoginForm
from backend.src.modules.users.service import UserService

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)


@router.post("/login")
async def login(
        form: LoginForm,
        response: Response,
        service: UserService = Depends(get_user_serv)
):
    user = await service.login(login_form=form, response=response)
    return {"user": user}
