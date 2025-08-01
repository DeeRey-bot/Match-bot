# Deploy на Render — Python 3.11

Этот проект специально подготовлен для исправления ошибки с `aiohttp` и Python 3.13.

## Что включено:
- `runtime.txt` — указывает версию Python 3.11.9
- `requirements.txt` — зафиксированная версия `aiohttp`
- `main.py` — тестовый код для проверки

## Как развернуть:
1. Залей папку на GitHub или Render
2. Убедись, что файлы `runtime.txt` и `requirements.txt` в корне
3. Render автоматически выберет Python 3.11.9
