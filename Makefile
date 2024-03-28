lint:
	poetry run black .
	poetry run isort .
	poetry run ruff check .
	poetry run mypy .
	