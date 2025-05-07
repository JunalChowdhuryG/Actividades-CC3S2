# **Actividad 12: Pruebas con Pytest y Fixtures**

Este proyecto implementa pruebas unitarias en Python utilizando `pytest` para validar la clase `Account` en `models/account.py`, con SQLAlchemy y datos en formato JSON. Se utilizan **fixtures** para configurar y limpiar el entorno de pruebas, y tambien  se generan informes de cobertura con `pytest-cov` y se utiliza un Makefile para facilitar la ejecucion de tareas localmente. Los informes de cobertura HTML se generan para visualizacion en el navegador

## **Logros**

- **Pruebas unitarias**: Implementadas con `pytest` para validar los metodos `create` y `all` de la clase `Account` en `models/account.py`
- **Uso de fixtures**: configuracion de fixtures a nivel de modulo, clase y metodo para inicializar la base de datos, cargar datos de prueba y limpiar el entorno
- **Cobertura de codigo**: Generada con `pytest-cov`, con informes detallados que muestran lineas no cubiertas
- **Gestion local**: `Makefile` para instalar dependencias, ejecutar pruebas, generar reportes de cobertura, realizar linting con `flake8` y limpiar archivos generados
- **Informes de cobertura**: Informe de cobertura en la terminal y un informe HTML en la carpeta `htmlcov/`, accesible abriendo `htmlcov/index.html`
- **Despliegue de reportes**: Informe de cobertura HTML publicado en GitHub Pages, accesible en:
  ```
  https://junalchowdhuryg.github.io/Actividades-CC3S2/Actividad-12/docs/
  ```

## **Uso**

Ubicado en la carpeta donde esta `Makefile`:

- **Instalar dependencias**:
  ```bash
  make install
  ```
  Instala `pytest`, `pytest-cov`, `sqlalchemy`, `Flask` y `flake8`.

- **Ejecutar pruebas unitarias**:
  ```bash
  make test
  ```
  Ejecuta todas las pruebas en `tests/test_account.py` con salida detallada. Ejemplo de salida:

- **Ejecutar pruebas con detencion en el primer fallo**:
  ```bash
  make test-exitfirst
  ```
  Detiene la ejecucion en el primer fallo, util para depuracion

- **Generar informe de cobertura**:
  ```bash
  make cov
  ```
  Genera un informe de cobertura en la terminal y un informe HTML en `htmlcov/`. Abre `htmlcov/index.html` en un navegador para visualizarlo

- **Ejecutar linting con flake8**:
  ```bash
  make lint
  ```
  Verifica el estilo del codigo y genera un reporte en `flake8-report.txt`

- **Limpiar archivos generados**:
  ```bash
  make clean
  ```
  Elimina archivos temporales como `.pytest_cache`, `.coverage`, `htmlcov/`, `__pycache__` y `test.db`

- **Ejecutar todas las tareas (instalacion, pruebas, cobertura)**:
  ```bash
  make all
  ```