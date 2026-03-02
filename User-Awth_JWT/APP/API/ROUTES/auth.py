from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from APP.SCHEMAS.user import UserCreate,UserOut,UserResponse

from APP.SCHEMAS.auth import Token

from APP.CRUD.user import(
    create_user,
    get_user_by_email
)

from APP.CORE.security import(
    hash_password,
    verify_password,
    create_access_token
)

from APP.API.desp import get_db

router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# registration of the user 

@router.post("/register",response_model=UserResponse)

def register(
    user:UserCreate,
    db:Session=Depends(get_db)
):
    existing_user=get_user_by_email(
        db,
        user.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email Already Registered"
        )
    
    new_user=create_user(
        db,
        user.email,
        user.username,
        user.password
    )

    return new_user


#  LOGIN for the userr


@router.post("/login",response_model=Token)

def login(
    email:str,
    password:str,
    db:Session=Depends(get_db)
):
    user=get_user_by_email(
        db,
        email
    )

    if not user:
        raise HTTPException(
            status_code=400,
            details="Invalid Creadentials!!!"
        )
    
    if not verify_password(
        password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=400,
            details="Invalid Creadential!!"
        )
    
    token=create_access_token(
        {"sub":str(user.id)}
    )

    return {
        "access_token":token,
        "token_type":"bearer"
    }