import pytest

from app.database.database import collection_name


@pytest.fixture()
def clean_db():
    collection_name.delete_many({})