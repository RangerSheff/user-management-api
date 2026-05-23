from app.core.config import Settings


def test_settings_default_values():
    settings = Settings(
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
        POSTGRES_USER="postgres",
        POSTGRES_PASSWORD="password",
        POSTGRES_HOST="localhost",
        POSTGRES_PORT=5432,
        POSTGRES_DB="user_management_db"
    )

    expected_url = (
        "postgresql+psycopg2://"
        "postgres:password@localhost:5432/user_management_db"
    )

    assert settings.DATABASE_URL == expected_url