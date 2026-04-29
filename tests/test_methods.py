import pytest

@pytest.mark.parametrize("case_name, payload", [
    ("Простые данные", {"name": "Alice", "age": 25}),
    ("Булево и дробь", {"is_active": True, "score": 98.5}),
    ("Вложенность", {"tags": ["python", "qa"], "meta": {"v": "1.0"}}),
    ("Пустой запрос", {})
])
def test_methods(api_session, base_url, timeout, case_name, payload):
    response = api_session.post(f"{base_url}/post", json=payload, timeout=timeout)
    assert response.json()["json"] == payload