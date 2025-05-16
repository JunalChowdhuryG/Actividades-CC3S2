# **Actividad 14: Factory y Fakes**

Esta actividad implementa pruebas unitarias en Python utilizando `pytest` y la biblioteca **FactoryBoy** para generar datos falsos y probar la clase `Account` en `models/account.py`. Se utilizan **factories** con la clase `Faker` y atributos `Fuzzy` para crear datos de prueba realistas  , reemplazando datos estaticos codificados. Tambien se incluye un `Makefile` para automatizar tareas como la instalacion de dependencias  , ejecucion de pruebas  , generacion de informes de cobertura y linting.

## **Logros**

- **pruebas unitarias**: implementadas con `pytest` para validar los metodos `create`  , `all`  , `to_dict`  , `from_dict`  , `update` y `delete` de la clase `Account` en `models/account.py`
- **Uso de FactoryBoy**: creacion de una clase `AccountFactory` en `tests/factories.py` que utiliza `Faker` y `Fuzzy` para generar datos falsos para los campos `id`  , `name`  , `email`  , `phone_number`  , `disabled` y `date_joined`
- **eliminacion de datos estaticos**: sustitucion de datos codificados (como `ACCOUNT_DATA` en `tests/fixtures/account_data.json`) por instancias dinamicas generadas con `AccountFactory`
- **cobertura de codigo**: generada con `pytest-cov`  , con informes detallados en la terminal y en formato HTML en la carpeta `htmlcov/`  , accesible abriendo `htmlcov/index.html`
- **Gestion local**: `Makefile` para instalar dependencias  , ejecutar pruebas  , generar reportes de cobertura  , realizar linting con `flake8` y limpiar archivos generados
- **Pruebas robustas**: casos de prueba actualizados para usar `AccountFactory`  , permitiendo la creacion de multiples cuentas y pruebas de escenarios como actualizacion con ID invalido
- **Despliegue de reportes:** informe de cobertura HTML publicado en GitHub Pages accesible en:
https://junalchowdhuryg.github.io/Actividades-CC3S2/Actividad-14/docs/


## **Uso**

Ubicado en la carpeta raiz del proyecto donde se encuentra el `Makefile`:

- **Instala dependencias**:
  ```bash
  make install
  ```
  Instala `pytest`  , `pytest-cov`  , `factory-boy`  , `faker`  , `sqlalchemy`  , `flake8` y otras dependencias necesarias.

- **Ejecuta pruebas unitarias**:
  ```bash
  make test
  ```
  Ejecuta todas las pruebas en `tests/test_account.py` con salida detallada

- **Ejecuta pruebas con detencion en el primer fallo**:
  ```bash
  make test-exitfirst
  ```
  Detiene la ejecucion en el primer fallo  , util para depuracion.

- **genera informe de cobertura**:
  ```bash
  make cov
  ```
  Genera un informe de cobertura en la terminal y un informe HTML en `htmlcov/`. Abre `htmlcov/index.html` en un navegador para visualizarlo.

- **ejecuta linting con flake8**:
  ```bash
  make lint
  ```
  Verifica el estilo del codigo y genera un reporte en `flake8-report.txt`.

- **Limpia archivos generados**:
  ```bash
  make clean
  ```
  elimina archivos temporales como `.pytest_cache`  , `.coverage`  , `htmlcov/`  , `__pycache__` y otros generados durante las pruebas.

- **ejecuta todas las tareas (instalacion  , prueebas  , cobertura)**:
  ```bash
  make all
  ```


## **Detalles de Implementacion**

- **FactoryBoy**: La clase `AccountFactory` utiliza `Faker` para generar nombres  , correos y numeros de telefono realistas  , y `FuzzyChoice`/`FuzzyDate` para valores aleatorios de `disabled` y `date_joined`.
- **Pruebas actualizadas**:
  - `test_crear_todas_las_cuentas`: crea 10 cuentas con `AccountFactory` y verifica que se almacenen correctamente.
  - `test_crear_una_cuenta`:crea una cuenta y verifica que se registre.
  - `test_to_dict`: valida la serializacion de una cuenta a diccionario.
  - `test_from_dict`: comprueba la deserializacion desde un diccionario.
  - `test_actualizar_una_cuenta`: verifica la actualizacion de una cuenta existente.
  - `test_id_invalido_al_actualizar`: prueba que se lance una excepcion al intentar actualizar con un ID invalido.
  - `test_eliminar_una_cuenta`: confirma que una cuenta se elimina correctamente.
