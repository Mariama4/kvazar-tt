class Config(object):
    """Base config."""

    TESTING: bool = False
    SQLALCHEMY_DATABASE_URI: str = ""


class ProductionConfig(Config):
    """Uses production config."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///kvazar_prod.db"


class DevelopmentConfig(Config):
    """Uses development config."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///kvazar_dev.db"


class TestingConfig(Config):
    """Uses test config."""

    SQLALCHEMY_DATABASE_URI = "sqlite://:memory:"
    TESTING = True

