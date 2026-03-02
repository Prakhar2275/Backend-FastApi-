from sqlalchemy.orm import Session
from APP.MODELS.user import User
from APP.CORE.security  import hash_password

def create_user(db,email,username,password):
    user=User(
        email=email,
        username=username,
        hash_password=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_email(db,email):
    return db.query(User).filter(
        User.email==email
    ).first()