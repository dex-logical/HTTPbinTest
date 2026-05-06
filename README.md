# HTTPbinTest

Учебный проект для отработки навыков автотестирования API на Python (pytest + requests).

##  Стек
- Python 3.10+
- pytest, requests
- httpbin.org (публичный тестовый API)

##  Структура

├── conftest.py # Фикстуры: сессия, base_url, timeout

├── requirements.txt

├── README.md

└── tests/
├── test_status_codes.py # Проверка статус-кодов

├── test_methods.py # POST-запросы с данными

├── test_headers.py # Работа с заголовками

└── test_errors.py # Обработка таймаутов


##  Особенности
- Фикстуры в `conftest.py` для переиспользования кода
- Параметризация тестов через `@pytest.mark.parametrize`
- Обработка ошибок через `pytest.raises`
- Использование `requests.Session` для эффективности

##  Запуск
```bash
# 1. Создать виртуальное окружение
python -m venv venv

# 2. Активировать (Windows)
venv\Scripts\activate

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Запустить тесты
pytest -v