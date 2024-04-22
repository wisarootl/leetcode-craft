lint:
	poetry run black .
	poetry run isort .
	poetry run ruff check .
	poetry run mypy .

test:
	poetry run pytest --cov=leetcode_craft --cov-report=term --cov-report=xml