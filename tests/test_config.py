from app.core.config import Settings


def test_settings_default_values():
    settings = Settings(
        APP_ENV="dev",
        LOG_LEVEL="INFO",
        POSTGRES_USER="postgres",
        POSTGRES_PASSWORD="password",
        POSTGRES_DB="user_management_db"
    )

    assert settings.APP_ENV == "dev"
    assert settings.LOG_LEVEL == "INFO"
    assert settings.POSTGRES_HOST == "localhost"
    assert settings.POSTGRES_PORT == 5432


def test_database_url_generation():
    settings = Settings(
        APP_ENV="test",
        LOG_LEVEL="INFO",
        POSTGRES_USER="test_user",
        POSTGRES_PASSWORD="test_password",
        POSTGRES_HOST="localhost",
        POSTGRES_PORT=5432,
        POSTGRES_DB="test_db"
    )

    expected_url = (
        "postgresql+psycopg2://"
        "test_user:test_password@localhost:5432/test_db"
    )

    assert settings.DATABASE_URL == expected_url