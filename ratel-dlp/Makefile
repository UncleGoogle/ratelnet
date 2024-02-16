.PHONY: lock install tests

init:
	python -m venv .venv
	. .venv/bin/activate
	pip install -U pip
	pip install pip-tools

install:
	. .venv/bin/activate
	pip install -r requirements-dev.txt

lock:
	pip-compile --output-file=requirements.txt --strip-extras reqs.in
	pip-compile --output-file=requirements-dev.txt --strip-extras reqs-dev.in

tests:
	. .venv/bin/activate
	python -m pytest -vv

wheel:
	python -m pip wheel .
