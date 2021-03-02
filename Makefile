setup:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip3 install -r requirements.txt; \

run:
	. venv/bin/activate; \
	python3 aws_report.py; \

freeze:
	. venv/bin/activate; \
	pip3 install black boto3 flake8 pylint pytest pytest-xdist requests --upgrade; \
	pip3 freeze > requirements.txt; \

format:
	. venv/bin/activate; \
	black *.py; \

lint:
	. venv/bin/activate; \
	flake8 --ignore E501,W503 *.py; \
	pylint --disable=C,R *.py; \

check: format lint

test:
	. venv/bin/activate; \
	pytest -n auto -v; \

retest:
	. venv/bin/activate; \
	pytest -n auto -v --lf; \

.PHONY: check format freeze lint run setup test
