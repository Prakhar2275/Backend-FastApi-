from fastapi import Depends,HTTPException
from jose import jwt,JWTError
from APP.CORE.config import SECRET_KEY,ALGORITHAM

from sqlalchemy.orm import Session
from APP.API.desp import get_db

from APP.MODELS.user import  User

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme=OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def get_current_user(
        token:str=Depends(oauth2_scheme),
        db:Session=Depends(get_db)
):
    try:
        payload=jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHAM]
            
        )

        user_id=payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )
        
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
    

    user=db.query(User).filter(
        user.id==int(user_id)
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not Found!!!"
        )
    
    return user


