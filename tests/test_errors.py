import pytest
import requests

def test_errors(api_session, base_url):
    with pytest.raises(requests.exceptions.Timeout):
        url = f"{base_url}/delay/3"
        response = api_session.get(url, timeout = 1)
