# Makefile para la actividad 14  Factory y fakes

# variables
PYTHON = python
PIP = pip
TEST_DIR = tests
COV_DIR = htmlcov
FLAKE_REPORT = flake8-report.txt

# instalar dependencias
install:
	$(PIP) install -r requirements.txt

# ejecutar pruebas
test:
	$(PYTHON) -m pytest $(TEST_DIR) -v

# ejecutar pruebas con detención en el primer fallo
test-exitfirst:
	$(PYTHON) -m pytest $(TEST_DIR) -v --exitfirst

# generar informe de cobertura
cov:
	$(PYTHON) -m pytest $(TEST_DIR) --cov=models --cov-report=term --cov-report=html

# ejecutar linting con flake8
lint:
	$(PYTHON) -m flake8 models tests > $(FLAKE_REPORT) || true

# limpiar archivos generados
clean:
	rm -rf .pytest_cache .coverage $(COV_DIR) __pycache__ */__pycache__ $(FLAKE_REPORT) htmlcov test.db

# ejecutar todas las tareas
all: install test cov lint

.PHONY: install test test-exitfirst cov lint clean all