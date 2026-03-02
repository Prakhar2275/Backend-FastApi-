import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")
SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHAM=os.getenv("ALGORITHAM")

ASSESS_TOKEN_EXPIRE_MINUTES=int(
    os.getenv("ASSESS_TOKEN_EXPIRE_MINUTES")
)
