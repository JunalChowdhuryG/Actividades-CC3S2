# CHANGELOG.md
## Dia 1 - 08-04-2025 - Configuracion inicial del entorno y estructura

- Se creo la carpeta del proyecto `PRUEBA_ENTRADA_CC3S2`
- Se instalo y configuro entorno virtual con FastAPI, Uvicorn, asyncpg, databases
- Se creo archivo `Dockerfile` para la app
- Se configuro `docker-compose.yml` con los servicios `app` y `db`
- Se incluyo el script `db/init.sql` con creacion de tabla `questions` y datos iniciales
- Se valido que el contenedor `db` se levanta correctamente y la tabla se crea con datos cargados
- Se creo la rama `feature/dia1` a partir de `develop`
- Se realizo merge a `develop` y se agrego tag `v1.0-day1`

**Tag asociado:** `v1.0-day1`

## Dia 2 - 09-04-2025 - Implementacion de modelo `Question`, conexion a base de datos y pruebas unitarias
- Se creo la clase `Question` en el archivo `question.py` con los atributos `description`, `options`, `correct_index` y `difficulty`, y el metodo `is_correct()`
- Se implemento la funcion `get_questions_from_db()` en `database.py` para recuperar preguntas desde PostgreSQL usando `psycopg2`
- Tambien agrego manejo de errores en `is_correct()` para lanzar excepcion `TypeError` si el indice de respuesta no es un entero
- se organizo los archivos en modulos separados: `question.py`, `database.py`, y `main.py`
- se escribieron pruebas unitarias para la clase `Question` en `tests/test_question.py` utilizando `pytest`
- se agrego un test de integracion para validar que `get_questions_from_db()` retorna una lista de preguntas validas desde la base de datos
- se incluyo `pytest` en `requirements.txt`
- se configuro un nuevo servicio `test` en `docker-compose.yml` para ejecutar pruebas automaticamente dentro del entorno Docker
- se actualizo el `Dockerfile` para soportar pruebas y estructuras modulares
- se verifico que los tests se ejecuten correctamente con el comando `docker-compose run --rm test`
- se creo la rama `feature/dia2` desde `develop`, se integraron los cambios y se realizo merge a `develop`
- se agrego tag `v1.0-day2`

**Tag asociado:** `v1.0-day2`

## Dia 3 - 10-04-2025 - Implementacion de la clase `Quiz` con sus pruebas unitarias y flujo basico del juego
- Implementacion de la clase `Quiz` con sus pruebas unitarias en `test_quiz`
- en la funcion `main()` se simula el flujo basico del juego mostrando preguntas en consola
- Conexion con la logica de `Question` y obtencion de preguntas desde la base de datos
- Se creo la rama `feature/dia-3-4-estructura-basic` desde `develop`, donde se trabajara el dia 3 y 4, se integraron los cambios y se realizo merge a `develop`
- se agrego el tag `v1.0-day3`

**Tag asociado:** `v1.0-day3`

## Dia 4 - 11-04-2025 - Sistema de puntuacion, manejo de rondas y finalizacion del juego
- En el dia 4 se continuo trabajando en la rama `feature/dia-3-4-estructura-basic`
- se implemento el  sistema de puntuacion, el manejo de rondas y la finalizacion del juego
- Implementacion del metodo `answer_question` para la clase `Quiz` con sus pruebas unitarias
- se añadio mas preguntas a la base de datos
- Refactorizacion al metodo `get_questions_from_db` para que filtre por dificultad opcionalmente y se añadio pruebas unitarias al nuevo funcionamiento
- se implemento la funcion `run_quiz()` en `main.py` para simular el juego trivia para una ronda de preguntas la cual es validada y contabilizada con la nueva caracteristica  `answer_question`
- se hizo los commits correspondiente a la rama `feature/dia-3-4-estructura-basic` y se procedio hacer el merge a `develop`
- se agrego el tag `v1.0-day4`

**Tag asociado:** `v1.0-day4`

## Dia 5- 12-04-2025 - Mejoras en la interfaz de usuario y refinamientos

- En el dia 5 se trabajo en la rama `feature/dia5-ui-improvements` 
- se modifico las presguntas `questions` de la base de datos para tener al menos 10 preguntas por cada nivel de dificultad
- se mejoro la interfaz de terminal para un juego `Quiz` mas fluido, con la nueva funcionalidad en el  que el usuario puede elegir el nivel dificultad
- se creo una interfaz de navegador con las mismas funcionalidades que la interfaz de terminal  utilizando `Flask`
- se creo los `templates` para la interfaz de navegador
- se documento las interaciones con las interfaces de usuario en `EVIDENCE`
- se hizo los commits correspondiente a la rama `feature/dia5-ui-improvements` y se procedio hacer el merge a `develop`
- se agrego el tag `v1.0-day5`

**Tag asociado:** `v1.0-day5`

## Dia 6- 13-04-2025  - Pipeline CI/CD y pruebas de integración

- En el dia 6 se trabajo en la rama `feature/dia6-ci-cd-integration` 
- Se creo las prueba de integracion en `app/tests/integration/test_integration.py`
- Se creo el `workflows` de github en `.github\workflows\ci.yml`
- Se hizo las pruebas de integracion correspondiente
- Se encontro fallos en la configuracion de SonarQube
- Se verifico que todos los test pasaran  
- se hizo los commits correspondiente a la rama `feature/dia6-ci-cd-integration` y se procedio hacer el merge a `develop`
- se agrego el tag `v1.0-day6`

**Tag asociado:** `v1.0-day6`

## Dia 7- 14-04-2025  - Pipeline CI/CD y pruebas de integracion
- Se corrigio los fallos encontrados en el dia 6 en SonarQube.
- Se cambio SonarQube por SonarCloud
- Se refactorizo los `templates`:
    - `index.html`: Menu principal, en donde se elige la dificultad
    - `question.html`: Seccion del quiz, donde se hacen las preguntas
    - `results`: Muestran los resultados finales
- Se refactorizo algunas pruebas unitarias y se agrego pruebas de integracion a flask para la creacion de la app
- Se creo el `.env` para el manejo de contenido sencible
- Se verifico que todos los 16 test pasaran
- Se implemento CI con el  `.github\workflows\ci.yml`
- Se actualizo requeriments.txt
- Se implemnto SonarCloud
- Se implemento Bandit y se mejoro la calidad de codigo en base a las observaciones de este mismo
- se hizo los commits correspondiente a la rama `feature/dia7` y se procedio hacer el merge a `develop`
- se agrego el tag `v1.0-day7`
- Se proyecta a implementar la funcionalidad del manejo de usuarios (user-password) utilizando cifrado y postgres **(A futuro)**

**Tag asociado:** `v1.0-day7`

## Final - 15-04-2025  - Pipeline CI/CD y pruebas de integracion

- Se creo la rama `qa/coverage-threshold` para manejar las pruebas unitarias y de integracion
- Se valido que la cobertura de código supere el 90%
- Se realizo documentación final y el merge final a main con tagging