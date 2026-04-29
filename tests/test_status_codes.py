import pytest

@pytest.mark.parametrize("endpoint, expected_status", [
    ("/get", 200),
    ("/status/404", 404),
    ("/status/500", 500)
])
def test_check_status_code(api_session, base_url, timeout, endpoint, expected_status):
    url = f"{base_url}{endpoint}"
    response = api_session.get(url, timeout=timeout)
    assert response.status_code == expected_status