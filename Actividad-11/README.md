# **Actividad 11: Pruebas Pytest con Aserciones**

Este proyecto implementa pruebas unitarias en Python utilizando `pytest` para validar una implementacion de una pila (`stack.py`). Se generan informes de cobertura con `pytest-cov` y se utiliza un `Makefile` para facilitar la ejecucion de tareas localmente. Los informes de cobertura HTML se generan para visualizacion en el navegador

## **Logros**
- **Pruebas unitarias**: Implementadas con `pytest` para validar los metodos `push`, `pop`, `peek` e `is_empty` en `src/stack.py`.
- **Cobertura de codigo**: Generada con `pytest-cov`, con informes detallados que muestran lineas no cubiertas.
- **Gestion local**: `Makefile` para instalar dependencias, ejecutar pruebas, generar reportes de cobertura y limpiar archivos generados.
- **Informes de cobertura**: Informe de cobertura en la terminal y un informe HTML en la carpeta `htmlcov/`, accesible abriendo `htmlcov/index.html`.
- **Despliegue de reportes**: informe de cobertura HTML publicado en `github pages`, accesible en:
```
https://junalchowdhuryg.github.io/Actividades-CC3S2/Actividad-11/docs/
```

## **Uso**
Ubicado en la carpeta donde esta `Makefile`:

El `Makefile` tiene comandos para gestionar:

- **Instalar dependencias**:
  ```bash
  make install
  ```
  Instala `pytest` y `pytest-cov`.

- **Ejecutar pruebas unitarias**:
  ```bash
  make test
  ```
  Ejecuta todas las pruebas en `tests/test_stack.py` con salida detallada.

- **Ejecutar pruebas con detencion en el primer fallo**:
  ```bash
  make test-exitfirst
  ```
  Detiene la ejecucion en el primer fallo, util para depuracion.

- **Generar informe de cobertura**:
  ```bash
  make test-cov
  ```
  Genera un informe de cobertura en la terminal y un informe HTML en la carpeta `htmlcov/`. Abre `htmlcov/index.html` en un navegador para visualizarlo

- **Limpiar archivos generados**:
  ```bash
  make clean
  ```
  Elimina archivos temporales como `.pytest_cache`, `.coverage`, `htmlcov/`, y `__pycache__`.

- **Ejecutar todas las tareas (instalacion, pruebas, cobertura)**:
  ```bash
  make all
  ```

