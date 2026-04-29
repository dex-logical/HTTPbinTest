import pytest
import requests

@pytest.fixture()
def base_url():
    return "https://httpbin.org"

@pytest.fixture()
def api_session(base_url, timeout):
    session = requests.Session()
    session.base_url = base_url
    session.default_timeout = timeout
    yield session
    session.close()

@pytest.fixture()
def timeout():
    return 5