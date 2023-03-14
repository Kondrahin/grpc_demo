# Инструкция по развертыванию

1. Установить зависимости - `poetry shell && poetry install`
2. Запустить redis - `docker run --name demo-redis -p 6379:6379 -d redis`
3. Запустить сервер - `python grpc_demo_server.py`
4. Запустить клиент - `python grpc_demo_client.py`
