import pytest
import requests

def test_timeout_raises_exception(api_session, base_url):
    with pytest.raises(requests.exceptions.Timeout):
        url = f"{base_url}/delay/3"
        api_session.get(url, timeout=1)