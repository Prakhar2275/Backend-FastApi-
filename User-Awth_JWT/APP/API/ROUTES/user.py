from fastapi import APIRouter,Depends

from APP.CORE.dependecies import get_current_user

from APP.MODELS.user import User

router=APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me")

def get_me(
    current_user:User=Depends(get_current_user)
):
    return current_user