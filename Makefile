install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code

lint:
	poetry run flake8

check:
	poetry run flake8
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
