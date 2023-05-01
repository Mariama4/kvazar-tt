from app import create_app
from config import ProductionConfig, TestingConfig


def test_config():
    assert not create_app(ProductionConfig).testing
    assert create_app(TestingConfig).testing
