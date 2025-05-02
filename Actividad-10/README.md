# **Actividad 10: Pruebas Pytest**

Este proyecto implementa pruebas unitarias en Python utilizando  `pytest`, genera informes de cobertura con `pytest-cov`, y verifica la calidad del codigo con `flake8` tambien incluye un flujo de trabajo automatizado en `github actions` y un `Makefile` para facilitar la ejecucion de tareas localmente. Los informes de cobertura HTML se publican en GitHub Pages para visualizacion en el navegador

## **Logros**
* pruebas unitarias: implementadas con pytest para validar el codigo en `triangle.py`
* cobertura de codigo: generada con `pytest-cov`, con informes detallados que muestran lineas no cubiertas
* verificacion de estilo: realizada con `flake8` para garantizar codigo limpio y consistente
* automatizacion: flujo de trabajo en `gitHub actions` que ejecuta pruebas, verifica estilo y publica resultados en cada `push` o `pull_request` a la rama main
* despliegue de reportes: informe de cobertura HTML publicado en `github pages`, accesible en: 
```
https://junalchowdhuryg.github.io/Actividades-CC3S2/
```
* artefactos: generados y disponibles en `github actions`:
* `flake8-report.txt`: Errores de estilo
* `htmlcov/`: informe de cobertura HTML
* gestion local: `Makefile` para ejecutar pruebas, verificar estilo y generar reportes facilmente

## USO
Ubicado en la carpeta donde esta `Makefile`

El `Makefile` tiene comandos para gestionar:

- **instalar dependencias**:
  ```bash
  make install
  ```

- **verificar estilo del codigo con `flake8`**:
  ```bash
  make lint
  ```
  Genera un informe en `flake8-report.txt`.

- **ejecutar pruebas unitarias**:
  ```bash
  make test
  ```

- **ejecuta pruebas de cobertura**:
  ```bash
  make test-cov
  ```
  genera un informe de cobertura en la terminal y un informe HTML en la carpeta `htmlcov/` solo  abre `htmlcov/index.html` 

- **limpia archivos generados**:
  ```bash
  make clean
  ```

- **ejecutar todas las tareas (instalacion, linting, pruebas)**:
  ```bash
  make all
  ```


