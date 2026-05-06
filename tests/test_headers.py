import pytest

def test_custom_headers(api_session, base_url, timeout):
    custom_headers = {"X-Test-Header": "qa-intern-2026"}

    url = f"{base_url}/headers"
    response = api_session.get(url, headers=custom_headers, timeout=timeout)
    assert response.status_code == 200

    assert response.json()["headers"]["X-Test-Header"] == "qa-intern-2026"