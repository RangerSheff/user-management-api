from app.core.config import Settings


def test_settings_default_values():
    settings = Settings(_env_file=".env.test")

    assert settings.POSTGRES_USER
    assert settings.POSTGRES_PASSWORD
    assert settings.POSTGRES_HOST
    assert settings.POSTGRES_DB
    assert settings.POSTGRES_PORT == 5432


def test_database_url_generation():
    settings = Settings(_env_file=".env.test")

    expected_url = (
        f"postgresql+psycopg2://"
        f"{settings.POSTGRES_USER}:"
        f"{settings.POSTGRES_PASSWORD}@"
        f"{settings.POSTGRES_HOST}:"
        f"{settings.POSTGRES_PORT}/"
        f"{settings.POSTGRES_DB}"
        f"?sslmode={settings.POSTGRES_SSLMODE}"
    )

    assert settings.DATABASE_URL == expected_url
