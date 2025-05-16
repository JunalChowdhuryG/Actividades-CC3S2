# **Actividad 13: Objetos Mocking**

Este proyecto implementa pruebas unitarias en Python utilizando `pytest` y la biblioteca `unittest.mock` para validar la clase `IMDb` en `models/imdb.py` . Se utilizan **fixtures** para cargar respuestas simuladas de la API de IMDb desde un archivo JSON y **mocking** para simular llamadas a servicios externos  evitando depender de la API real durante las pruebas. Tambien se incluye un `Makefile` para facilitar la ejecucion de tareas localmente

## **Logros**

- **Pruebas unitarias**: Implementadas con `pytest` para validar los metodos `search_titles()` `movie_reviews()` y `movie_ratings()` de la clase `IMDb` en `models/imdb.py`
- **Uso de fixtures**: Configuracion de una fixture a nivel de sesion (`imdb_data`) para cargar respuestas simuladas desde `tests/fixtures/imdb_responses.json` permitiendo pruebas controladas y repetibles
- **Mocking y patching**: Uso de `@patch` y la clase `Mock` de `unittest.mock` para simular las respuestas de la biblioteca `requests` y evitar llamadas reales a la API de IMDb
- **Casos de prueba variados**: Pruebas para escenarios de exito (busqueda exitosa calificaciones validas) fallos (clave de API invalida) y casos sin resultados (titulos inexistentes)
- **Gestion local**: `Makefile` para instalar dependencias ejecutar pruebas realizar linting con `flake8` y limpiar archivos generados
- **Cobertura de codigo**: Generada con `pytest-cov` con informes detallados que muestran la cobertura de las pruebas
- **Despliegue de reportes**: Informe de cobertura HTML publicado en GitHub Pages accesible en:
```
https://junalchowdhuryg.github.io/Actividades-CC3S2/Actividad-13/docs/
```

## **Uso**

Ubicado en la carpeta raiz del proyecto donde se encuentra el `Makefile` de la Actividad 13:

- **Instalar dependencias**:
  ```bash
  make install
  ```
  Instala `pytest` `pytest-cov` `requests` `flake8` y otras dependencias necesarias

- **Ejecutar pruebas unitarias**:
  ```bash
  make test
  ```
  Ejecuta todas las pruebas en `tests/test_imdb.py` con salida detallada

- **Ejecutar pruebas con detencion en el primer fallo**:
  ```bash
  make test-exitfirst
  ```
  Detiene la ejecucion en el primer fallo util para depuracion

- **Generar informe de cobertura** (si esta configurado):
  ```bash
  make cov
  ```
  Genera un informe de cobertura en la terminal y un informe HTML en `htmlcov/` Abre `htmlcov/index.html` en un navegador para visualizarlo

- **Ejecutar linting con flake8**:
  ```bash
  make lint
  ```
  Verifica el estilo del codigo y genera un reporte en `flake8-report.txt`

- **Limpiar archivos generados**:
  ```bash
  make clean
  ```
  Elimina archivos temporales como `.pytest_cache` `.coverage` `htmlcov/` `__pycache__` y otros generados durante las pruebas

- **Ejecutar todas las tareas (instalacion pruebas cobertura)**:
  ```bash
  make all
  ```

## **Detalles de Implementacion**

- **Fixtures**: La fixture `imdb_data` carga las respuestas simuladas desde `imdb_responses.json` para simular diferentes escenarios de la API (exito , fallo , sin resultados)
- **Mocking**: Se utiliza `@patch` para interceptar las llamadas a `requests.get()` y simular respuestas HTTP con objetos `Mock` que imitan la clase `Response` de `requests`
- **Pruebas**:
  - `test_search_titles_success`: Valida una busqueda exitosa por titulo
  - `test_search_titles_failure`: Verifica el manejo de busquedas sin resultados
  - `test_movie_reviews_success`: Comprueba la obtencion de reseñas validas
  - `test_movie_ratings_success`: Valida la obtencion de calificaciones correctas
  - `test_search_by_title_failed`: Simula una busqueda con una clave de API invalida
  - `test_movie_ratings_good`: Confirma que las calificaciones se procesan correctamente
