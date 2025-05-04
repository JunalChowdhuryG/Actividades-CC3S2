# Makefile

# Variables
PYTHON = python
PIP = $(PYTHON) -m pip
PYTEST = $(PYTHON) -m pytest
COV = --cov=src
COV_REPORT = --cov-report=term-missing --cov-report=html
export PYTHONPATH := $(shell pwd)/src:$(PYTHONPATH)

# Instalar dependencias
install:
	$(PIP) install pytest pytest-cov

# Ejecutar pruebas
test:
	$(PYTEST) -v tests/

# Ejecutar pruebas con detención en el primer fallo
test-exitfirst:
	$(PYTEST) -x tests/

cov:
	$(PYTEST) --cov=src --cov-report=term-missing --cov-report=html tests/

# Limpiar archivos generados
clean:
	rm -rf .pytest_cache
	rm -rf .coverage
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	rm -rf htmlcov

# Ejecutar todas las tareas principales
all: install test cov

.PHONY: install test test-exitfirst cov clean all