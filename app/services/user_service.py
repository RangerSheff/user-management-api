from fastapi import HTTPException, status

from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_users(self):
        return self.repository.get_all()

    def get_user_by_id(self, user_id: str):
        user = self.repository.get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

        return user

    def create_user(self, user_data: UserCreate):
        if self.repository.get_by_email(user_data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Email already exists"
            )

        if self.repository.get_by_username(user_data.username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Username already exists"
            )

        return self.repository.create(user_data)

    def update_user(self, user_id: str, user_data: UserUpdate):
        user = self.repository.get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

        if user_data.email and user_data.email != user.email:
            existing_email = self.repository.get_by_email(user_data.email)
            if existing_email:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT, detail="Email already exists"
                )

        if user_data.username and user_data.username != user.username:
            existing_username = self.repository.get_by_username(user_data.username)
            if existing_username:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Username already exists",
                )

        return self.repository.update(user, user_data)

    def delete_user(self, user_id: str):
        user = self.repository.get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

        self.repository.delete(user)
        return None
