import importlib
from unittest.mock import patch

from app import database

def test_create_engine_called_with_correct_parameters():
    with patch('sqlalchemy.create_engine') as mock_create_engine:
        importlib.reload(database)
        mock_create_engine.assert_called_once_with(database.DATABASE_URL)

def test_sessionmaker_called_with_correct_parameters():
    with patch('sqlalchemy.orm.sessionmaker') as mock_sessionmaker:
        importlib.reload(database)
        mock_sessionmaker.assert_called_once_with(autocommit=False, autoflush=False, bind=database.engine)