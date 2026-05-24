import pytest

from app.core.config import settings
from app.db.database import Base, SessionLocal, engine
from app.models.user_model import User

TEST_USERNAME_PREFIX = "userTest"

Base.metadata.create_all(bind=engine)

def delete_test_users_only():
    db = SessionLocal()

    try:
        db.query(User).filter(
            User.username.like(f"{TEST_USERNAME_PREFIX}%")
        ).delete(synchronize_session=False)

        db.commit()
    finally:
        db.close()


@pytest.fixture(autouse=True)
def clean_test_users():
    if settings.APP_ENV == "prod":
        raise RuntimeError(
            "Tests cannot run in production environment."
        )

    delete_test_users_only()

    yield

    delete_test_users_only()