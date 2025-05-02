# variables
PYTHON = python
PIP = pip
PYTEST = pytest
COV = --cov=pruebas_pytest
COV_REPORT = --cov-report=term-missing --cov-report=html
FLAKE8 = flake8

# instalar dependencias
install:
	$(PYTHON) -m $(PIP) install --upgrade pip
	$(PYTHON) -m $(PIP) install pytest pytest-cov

# ejecutar  pruebas 
test:
	$(PYTEST) -v

# ejecutar flake8
lint:
	$(FLAKE8) . --output-file=flake8-report.txt
	@echo "Flake8 report generated at flake8-report.txt"

# ejecutar pruebas con informe  cobertura
test-cov:
	$(PYTEST) $(COV) $(COV_REPORT) -v

# limpia archivos generados
clean:
	rm -rf htmlcov .coverage __pycache__ .pytest_cache

# Ejecuta todas las tareas (instalación y pruebas con cobertura)
all: install test-cov

.PHONY: install test test-cov clean all
