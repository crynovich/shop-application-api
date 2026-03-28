from fastapi import APIRouter
from models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_users() -> list[User]:
    users = [
        User(name="marko", age=22),
        User(name="John", age=33),
        User(name="Alice", age=45),
    ]
    return users
