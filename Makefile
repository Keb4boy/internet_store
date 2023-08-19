create:
	alembic revision --autogenerate -m "db create"

upgrade:
	alembic upgrade head

start:
	poetry run uvicorn internet_store:app --host 0.0.0.0 --port 7778 --reload