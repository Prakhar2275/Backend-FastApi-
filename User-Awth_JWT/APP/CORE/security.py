from passlib.context import CryptContext

from jose import jwt

from datetime import datetime,timedelta

from APP.CORE.config import SECRET_KEY,ALGORITHAM,ASSESS_TOKEN_EXPIRE_MINUTES


pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password:str):
    password = password[:72]
    return pwd_context.hash(password)

def verify_password(plain,hashed):
    plain_password = plain_password[:72]
    return pwd_context.verify(plain,hashed)

def create_access_token(data:dict):
    expire=datetime.utcnow()+timedelta(
        minutes=ASSESS_TOKEN_EXPIRE_MINUTES
    )

    data.update({"exp":expire})

    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHAM
    )