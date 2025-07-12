# **Actividad-25: Arquitectura y desarrollo de microservicios con Docker y Kubernetes**


## **I. Conceptualizacion de microservicios**

### **1. ¿Por que microservicios?**

**1.1. Describe la evolucion historica desde arquitecturas monoliticas a SOA y finalmente microservicios**  
**Referencia**:
[Medium: The Evolution of Software Architecture: Monolithic to Microservices](https://medium.com/@phanindra208/the-evolution-of-software-architecture-monolithic-to-microservices-cb62fcd7aa94)

- **arquitectura monolitica:** las aplicaciones se diseñaban como un solo bloque donde todos los componentes como la llogica de negocio , interfaz de usuario , acceso a datos estaban acoplados en una unica base de codigo esto facilitaba el desarrollo inicial  pero a medida que las aplicaciones crecian, surgian problemas como tiempos de despliegue largos, dificultades para escalar componentes y cuellos de botella en el mantenimiento, ya que un cambio pequeño requeria redeplegar toda la aplicacion

- **Arquitectura orientada a servicios (SOA)**
SOA fue una respuesta al monolito proponiendo dividir la aplicacion en servicios independientes que se comunicaban a traves de interfaces SOA  sin embargo los servicios seguian teniendo cierto grado de acoplamiento lo que limitaba la flexibilidad

- **Microservicios**
los microservicios emergieron como una evolucion de SOA pero con un enfoque mas granular y descentralizado inspirados por practicas de DevOps y la nube, los microservicios dividen la aplicacion en servicios pequeños, independientes, cada uno con una unica responsabilidad, comunicandose mediante APIs ligeras


**1.2. Presenta dos ejemplos de casos de uso (por ejemplo, ecommerce con picos de demanda y aplicacion SaaS multi-tenant) donde el monolito se vuelve insostenible.**
- **E-commerce con picos de demanda** en un evento como black friday el monolito enfrenta problemas debido a su incapacidad para escalar componentes individuales por ejemplo para el modulo de procesamiento de pagos en un monolito, escalar implica repplicar toda la aplicacion lo que es costoso e ineficiente los microservicios permiten escalar solo el servicio de pagos opptimizando recursos y mejorando la experiencia del usuario

- **Aplicacion SaaS multi-tenant** 
en un monolito un cambio en un modulo puede afectar a todos los tenants despliegue de nuevas funcionalidades requiere pruebas exhaustivas de toda la aplicacion retrasando las entregas los microservicios permiten aislar la logica de cada tenant o funcionalidad  facilitando personalizaciones y despliegues independientes



### **2. Definiciones clave**
**2.1. Define un microservicio y enumera sus caracteristicas: despliegue independiente, enfoque en una unica responsabilidad, contrato a traves de APIs.**  

es una unidad de software pequeña e independiente que realiza una unica funcion o responsabilidad dentro de un sistema mas grande y se diseñan para ser autonomos, con su propia logica y datos y ciclo de vida y se comunican con otros servicios a traves de interfaces bien definidas

- **despliegue independiente:** cada microservicio puede desarrollarse y desplegarse y escalarse sin afectar a otros
- **unica responsabilidad:** se enfoca en una sola capacidad de negocio siguiendo el principio de responsabilidad unica **SRP**
- **contrato a traves de APIs:** la comunicacion se realiza mediante interfaces  REST, gRPC, mensajeria lo quee garantiaza bajo acoplamiento



**2.2. Define una aplicacion de microservicios: colecciones de servicios que colaboran, balanceadores, gateways, y elementos de observabilidad.**  
es un sistema compuesto por multiples microservicios que colaboran para cumplir los objetivos de negocio
- servicios: cada uno ejecuta una funcion especifica por ejemplo, autenticacion, pagos, etc
- balanceadores de carga: distribuyen el trafico entre instancias de un mismo servicio para mejorar la disponibilidad
- API Gateways: actuan como punto de entrada unico enrutando solicitudes a los servicios correspondientes y manejando autenticacion o rate-limiting
- elementos de observabilidad: herramientas como Prometeus  Grafana o Jaeger para monitoreo metricas y trazabilidad de solicitudes



### 3. **Criticas al monolito**

**3.1. Identifica dos problemas tipicos: tiempo de despliegue global (cadencia lenta) y acoplamiento que obstaculiza el escalado separado.**

- **tiempo de despliegue global (cadencia lenta)**: en un monolito cualquier cambio por mas pequeño que sea requiere redeplegar toda la aplicacion esto implica compilar y probar y desplegar todo el sistema lo que puede tomar horas o diass retrasando la entrega de nuevas funcionalidades

- **acoplamiento que obstaculiza el escalado separado:** como todos los componentes estan enlazados  no es posible escalar solo una parte de la aplicacion por ejemplo si el modulo de busqueda necesita mas recursos se debe escalar toda la aplicacion aumentando costos y complejidad


### 4. **Popularidad y beneficios**

**Fuente:** [Microservices Examples](https://blog.dreamfactory.com/microservices-examples)

**4.1. Explica por que grandes empresas (Netflix, Amazon) adoptaron microservicios.**

- Netflix: necesitaba manejar millones de usuarios simultaneos con alta disponibilidad los microservicios permitieron escalar servicios especificos como streaming o recomendaciones y aislar fallos asegurando que un problema en un servicio no afectara al resto

- Amazon: Paso de un monolito a microservicios para acelerar el desarrollo y permitir que equipos autonomos trabajaran en paralelo reduciendo dependencias y mejorando la velocidad de innovacion


**4.2. Detalla tres beneficios clave: resiliencia (fallos aislados), escalabilidad granular y aceleracion de equipos autonomos.**


1. **resiliencia (fallos aislados)**: Un fallo en un microservicio no afecta al sistema completo  por ejemplo si el servicio de recomendaciones falla el catalogo de productos sigue funcionando
2. **escalabilidad granular:** permite escalar solo los servicios con alta demanda optimizando recursos por ejemplo en un e-commerce  el servicio de pagos puede tener mas instancias durante picos de trafico
3. **aceleracion de equipos autonomos:** los equipos pueden trabajar en paralelo en diferentes servicios usando tecnologias adecuadas a cada caso lo que reduce cuellos de botella y acelera los despliegues


### **5. Desventajas y retos**

**5.1. Discute cuatro desafios: necesidad de habilidades para redes y seguridad, complejidad de orquestacion, consistencia de datos distribuidos y dificultades de testing.**

- **necesidad de habilidades para redes y seguridad:** los microservicios requieren gestionar comunicacion entre servicios por ejemplo balanceo de carga y asegurar cada servicio individualmente autenticacion, cifrado, lo que exige conocimientos avanzados

- **complejidad de orquestacion:** coordinar multiples servicios, sus dependencias y despliegues en entornos distribuidos es complejo herramientas como Kubernetes ayudanpero tienen una curva de aprendizaje

- **consistencia de datos distribuidos:** cada microservicio tiene su propia base de datos, lo que puede generar problemas de consistencia en transacciones distribuidas 

- **dificultades de testing:** probar una aplicacion de microservicios requiere simular interacciones entre servicios lo que puede ser mas complicado que probar un monolito


**5.2. Propon estrategias de mitigacion: utilizacion de contratos OpenAPI, pruebas contractuales, herramientas de trazabilidad (Jaeger) y patrones de sagas.**

- **contratos OpenAPI:** definir contratos claros para las APIs asegura que los servicios sean compatibles y facilita pruebas automatizadas

- **pruebas contractuales:** usar herramientas como Pact para verificar que los servicios cumplen con los contratos establecidos sreduciendo errores de integracion

- **herramientas de trazabilidad Jaeger:** implementar sistemas de trazabilidad distribuidos para monitorear solicitudes a traves de multiples servicios, identificando cuellos de botella o errores

- **patrones de sagas:** En lugar de transacciones distribuidas tradicionales usar sagas que son secuencias de transacciones locales con compensaciones para mantener la consistencia de datos


### **6. Principios de diseño**



**6.1. Explica el diseño orientado al dominio (DDD) y como ayuda a delimitar limites contextuales para servicios.**
  
**Referencia:** [Medium: Domain Driven Design](https://medium.com/@jonathanloscalzo/domain-driven-design-principios-beneficios-y-elementos-primera-parte-aad90f30aa35)


es una metodologia que alinea el diseño del software con el dominio del negocio en microservicios DDD ayuda a definir contextos acotados que son limites logicos donde un servicio tiene una unica responsabilidad y un modelo de datos propio Por ejemplo en un e-commerce el contexto de "pedidos" podria incluir la logica para crear y rastrear pedidos mientras que el contexto de "inventario" gestiona el stock DDD asegura que cada microservicio sea cohesivo y tenga un proposito claro  reduciendo el acoplamiento


**6.2. Analiza el principio DRY en microservicios: promover bibliotecas compartidas versus duplicacion controlada.**
  
**Referencia:** [Exploring the DRY Principle in Microservices Architecture](https://medium.com/@er.juveriamanzar/exploring-the-dry-principle-in-microservices-architecture-challenges-and-alternatives-6abc871c2bcc)

ll principio DRY (Don’t Repeat Yourself) busca evitar la duplicacion de codigo en microservicios hay un debate sobre como aplicarlo:

- **Bibliotecas compartidas:** crear bibliotecas comunes para logica reutilizable (por ejemplo, autenticacion o utilidades) puede reducir duplicacion, pero introduce dependencias entre servicios lo que contradice la autonomia actualizar una biblioteca requiere coordinar cambios en multiples servicios
- **Duplicacion controlada:** en varios casos es preferible duplicar pequeñas porciones de codigo en cada microservicio para preservar su independencia. Por ejemplo, cada servicio puede implementar su propia logica de validacion en lugar de depender de una biblioteca compartida la duplicacion debe ser minima y justificada


**6.3. Discute criterios para decidir el tamaño de un servicio (ej. regla de la "una tabla por servicio" o "una capacidad de negocio por servicio").**

el tamaño de un microservicio es clave para evitar servicios demasiado grandes tambien se llamaa mini-monolitos o demasiado pequeños cuando se exceden en fragmentación
  
**criterios:**

- **"una tabla por servicio"**: cada microservicio debería gestionar una única tabla o un conjunto pequeño de tablas relacionadas en su base de datos, para asuegurarse que el servicio sea cohesivo y tenga una sola responsabilidad **SRP**

- **capacidad de negocio por servicio:** un microservicio debe alinearse con una capacidad específica del negocio, como el procesar pagos o la gestionar inventario esto sigue los principios de DDD y facilita escalabilidad

- **tamaño manejable por un equipo:** un servicio debe ser lo  pequeño como para que un equipo pequeño  pueda desarrollarlo y mantenerlo sin fricciones



## **II. Empaquetado y publicación con Docker**

### **1. Creación de un Dockerfile**
El Dockerfile del proyecto:

```Dockerfile
# Etapa de construcción 
FROM python:3.12-slim AS builder

# Evitar archivos .pyc y forzar salida no bufferizada
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /build

# Copiar dependencias y resolverlas en el usuario actual
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


# Etapa de producción 
FROM python:3.12-slim AS production

# Usuario y grupo de la aplicación
ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} \
    && useradd -m -r -g ${APP_USER} ${APP_USER}

# Variables de entorno para el usuario no root
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/${APP_USER}/.local/bin:${PATH}"

WORKDIR /app

# Copiar binarios y dependencias instaladas
COPY --from=builder /root/.local /home/${APP_USER}/.local

# Copiar todo el código fuente
COPY . /app

# <- AÑADE ESTO para dar permisos sobre /app
RUN chown -R ${APP_USER}:${APP_USER} /app

# Ejecutar como usuario no root
USER ${APP_USER}

# Puerto expuesto por la aplicación
EXPOSE 80

# Comando por defecto
CMD ["uvicorn", "microservice.main:app", "--host", "0.0.0.0", "--port", "80"]
```

**1.1. Estructura multi-stage: etapa de builder (instalación de dependencias) y etapa de producción (imagen slim, usuario non-root).**

* etapa de builder `FROM python:3.12-slim AS builder`:
    - usa la imagen base `python:3.12-slim` para minimizar el tamaño
    - configura el directorio de trabajo en `/build`
    - copia `requirements.txt` e instala las dependencias con `pip install --user --no-cache-dir -r requirements.txt` la opción `--user` instala las dependencias en el directorio del usuario `/root/.local`  y `--no-cache-dir` evita almacenar caché de pip, reduciendo el tamaño de la imagen

* etapa de producción `FROM python:3.12-slim AS production`:
    - usa la misma imagen base ligera para consistencia
    - crea un usuario no privilegiado `appuser` con `groupadd` y useradd para mejorar la seguridad, evitando ejecutar el contenedor como root
    - copia las dependencias instaladas desde `/root/.local` etapa builder a `/home/appuser/.local` y el código fuente completo a `/app`
    - ajusta los permisos del directorio /app con chown -R appuser:appuser /app para que el usuario no root tenga acceso
    - cambia al usuario appuser con `USER appuser` y expone el `puerto 80` donde la aplicación  escucha solicitudes



**1.2. Importancia de variables de entorno (PYTHONDONTWRITEBYTECODE, PYTHONUNBUFFERED) y de definir un ENTRYPOINT claro.**
* **Variables de entorno**
    - `PYTHONDONTWRITEBYTECODE=1`: evita la generación de archivos `.pyc` lo que reduce el tamaño de la imagen y previene problemas de permisos en volúmenes
    - `PYTHONUNBUFFERED=1`: desactiva el buffering de la salida estándar
    - `PATH="/home/${APP_USER}/.local/bin:${PATH}"`: añade el directorio de binarios del usuario 

* **CMD en lugar de ENTRYPOINT**
    - el `Dockerfile` usa CMD `["uvicorn", "microservice.main:app", "--host", "0.0.0.0", "--port", "80"]` para definir el comando por defecto  essto inicia el servidor FastAPI  vinculándolo al puerto 80



### **2. Empaquetado y Verificación**

**2.1. Comando de construcción: docker build -t ejemplo-microservice:0.1.0 . y opciones como --no-cache.**
- `docker build -t ejemplo-microservice:0.1.0 .` construye la imagen con el nombre ejemplo-microservice y la versión 0.1.0 desde el directorio actual siguiendo la estructura multi-stage del `Dockerfile` la opcion `--no-cache`  ignora la caché de capas estoo aseguraa que las dependencias se reinstalen desde cero

**2.2. Flujo de prueba: docker run -d -p 80:80 ejemplo-microservice:0.1.0 y curl -i http://localhost/api/items/ para validar status y payload.**
- `-i http://localhost/api/items/` esto verifica que la API responda correctamente


### **3. Depuración de contenedores**

**3.1. Visualización de logs en tiempo real: docker logs -f ejemplo-ms.**
- `docker logs -f ejemplo-ms` muestra los logs en tiempo real del contenedor gracias a `PYTHONUNBUFFERED=1` en el Dockerfile

### **5. Buenas prácticas de tags**

**5.1. Uso de SemVer (MAJOR.MINOR.PATCH) y tag latest para entornos de staging.**
- etiquetar imágenes con versiones `MAJOR.MINOR.PATCH`  para tenner claridad y trazabilidad y el tag `latest` se usa en entornos de staging para pruebas rápidas pero no utiliza en producción ya que no garantiza estabilidad


**5.2. Estrategias de limpieza: políticas de retención en el registry y docker image prune --filter "until=24h".**

- configurar políticas de retención en el registro para eliminar imágenes antiguas  un ejemplo seria mantener solo las últimas 5 versiones
- usar `docker image prune --filter "until=24h"` para eliminar lass imágenes  que no se utilizan creadas hace más de 24 horas optimizando espacio local


## **III. Desarrollo y despliegue avanzado**


### **1. Docker Compose para desarrollo**

#### **1.1. Fundamentos de Docker Compose**

##### **Teórico**

* **Explica qué ventajas aporta Compose frente al uso de `docker run` por separado (declaratividad, dependencias, redes).**
    - Docker compose es una herramienta que permite definir y gestionar múltiples contenedores de forma declarativa mediante archivo docker-compose.yml las ventajas sobre el `docker run` son:
        - **es declaratividad:** ya que  solo archivo YAML define servicios y redes y volúmenes y dependencias simplificando la configuración y reduciendo errores manuales a diferencia de varios comandos `docker run`
        - **la gestión de de dependencias**: ya uque permite especificar dependenciass entre servicios con `depends_on`
        - **las redes aisladas:** se crea automáticamente redes privadas para que los servicioss se comuniquen entre ellos

* **Define conceptos: servicios, volúmenes, redes, perfiles (`profiles`), y cómo Compose los orquesta.**

    - **servicios**: representa contenedores individuales donde cada servicio especifica su imagen , puerto  y variable de entorno y dependencias
    - **volúmenes**: los persisten datos como datos de una base de datos o montan código fuente para desarrollo 
    - **redes**: se definen redes privadas para la comunicación entre servicios
    - **perfiles** permiten ejecutar subconjuntos de servicios según el entorno 

##### **Ejercicio teórico**

1. **Enumera al menos tres escenarios donde Docker Compose facilite el flujo de desarrollo (p. ej., replicar entornos staging, pruebas de integración local, debugging con recarga en vivo).**

- **replicar entornos staging:** el compose define un entorno local con servicios idénticos a los de staging se asegura  que las pruebas locales repliquenn el comportamiento de producción esto reduce errores debido a diferencias de configuración

- **pruebas de integración local**: facilita probar interacciones entre servicios 

- **debugging con recarga en vivo:** usa bind mounts los cambios en el código fuente se reflejan instantáneamente lo que permitie depurar rápidamente sin teneer que reconstruir imágenes

2. **Justifica por qué usarías perfiles (`profiles`) para separar entornos "dev" y "test".**

- **perfil dev** se habilita la recarga en vivo (--reload) y se montan volúmene para código fuente esto optimiza la iteración rápida
- **perfil test** se usa configuracione optimisadas para pruebas  y se desactiva la recarga para simular un entorno más cerca a produccción


#### **1.2. Estructura de `docker-compose.yml`**

##### **Teórico**

* **Detalla la sintaxis de los bloques principales: `services`, `volumes`, `networks`.**

    - **services:** define  contenedores  incluye imagen , puertos y  variabless de entorno y volúmenes y dependencias
    - **volumes:** configura volúmenes nombrados para persistencia datos 
    - **networks:** especifica redes privadas para la comunicación entre servicios
* **Explica el uso de `depends_on`, variables de entorno y montajes (`bind mounts` vs `named volumes`).**

    - **depends_on:** indica el orden de arranque de los servicios
    - **variables de entorro:** configuran el comportamiento de los servicios
    - **Bind mounts vs named volumes** Bind mounts  montan un directorio del host en el contenedor esto refleja cambios en el codigo en tiempo real y named volumes persisten datos entre ejecuciones



##### **Ejercicio práctico (redacción)**

1. **Diseña por escrito un fragmento de `docker-compose.yml` que levante un servicio FastAPI con recarga en vivo y una base de datos Postgres, indicando:**

    * Cómo definirías el `bind mount` para el código fuente.
    * Qué usuario o permisos ajustarías dentro del contenedor para evitar problemas de escritura.

2. **Describe en palabras cómo Compose garantiza que la base de datos arranque antes que la API.**

    - el atributo `depends_on: [base_de_datos]` asegura que el servicio `base_de_datos` se inicie antes que el servicio `api` Docker Compose espera que el contenedor  base de datos esté en  "runing" antes de iniciar la API



#### **1.3. Flujo de trabajo con Compose**

##### **Teórico**

1. **Describe los comandos esenciales:**

    - **`docker-compose up --build`**: construye imágenes definidas en el `build` del `docker-compose.yml` levanta todos los servicios opción `--build` fuerza la reconstrucción de la imagen

    - **`docker-compose logs -f <servicio>`**: muestra logs en tiempo real de servicio específico   
    
    - **`docker-compose down --volumes`**: detiene y elimina todos los contenedores y redes y volúmenes definidos limpia el entorno la opción `--volumes` elimina datos persistentes



2.  **Explica el propósito de cada uno y efectos colaterales (p.ej., recreación de contenedores, limpieza de volúmenes).**
- **`up --build`**: reconstruye imágen pero puede aumentar el tiempo de inicio si la instalación  es lenta  
- **`logs -f`**: no afecta el estado de los contenedore consume recursos si se mantiene abierto por mucho tiempo
- **`down --volumes`**: elimina datos persistentes  puede ser destructivo en entorrnos con datos importantes



##### **Ejercicio práctico (manos a la obra)**

1. **Escribe en orden los comandos que usaría un desarrollador para:**
- **Iniciar en modo desarrollo con recarga**:  
  - `docker-compose --profile dev up --build`: levanta servicios con  perfil `dev` construye la imagen del `Dockerfile` habilita recarga en vivo para la API con `--reload`
- **Cambiar al perfil `staging` (sin recarga) y reiniciar solo la API**:  
  - `docker-compose --profile staging up -d api` levanta  el servicio `api` con el perfil `staging` usando el `CMD` del `Dockerfile`  simula  entorno producción
- **Detener todo y eliminar volúmenes**:  
  - `docker-compose down --volumes`: detiene los servicios y elimina contenedores y redes y volúmenes y  datos de la base de datos


2. **Pon en un pequeño script bash (`setup-dev.sh`) esos comandos con comentarios apropiados.**

    ```bash
    # entorno  modo desarrollo con recarga  vivo
    echo "incia entorno desarrollo"
    docker-compose --profile dev up --build

    # perfil staging sin recarga y reinicia solo la API
    echo "perfil staging y reinico API"
    docker-compose --profile stagging up -d api

    # detiene los servicios y elimina volúmenes
    echo "detiene servicios elimina volúmen"
    docker-compose down --volumes
    ```





