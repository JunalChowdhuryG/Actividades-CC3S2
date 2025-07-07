# **Actividad 27: Migrando a Microservicios  Docker, Kubernetes y CI/CD**

## **A. Docker y Docker Compose**


### 1. **Arquitectura de contenedores**

**Explica como un contenedor encapsula la aplicacion y sus dependencias. ¿Que ventajas ofrece frente a una VM en terminos de arranque, consumo de recursos y portabilidad?**

cada contenedor encapsula la app con sus dependencias ya sea bibliotecas, runtime , configuraciones y una porcion minima del sistema operativo que es el kernel compartido con el host tambien usa tecnologias como namespaces para aislar procesos, redes y sistemas de archivos  
En el proyecto los Dockerfile de `service-user` y `service-order` incluyen `Python 3.10`, `fastapi`, `uvicorn`, `pydantic` y el codigo de la aplicacion, garantizando que el entorno sea identico en cualquier maquina.

**Ventajas frente a una VM:**

- **arranque**: los contenedores inician en segundos ya que al no cargar un SO completo  en comparacion con VM
- **consumo de recursos**: los contenedores comparten el kernel del host lo que  usa menos CPU y memoria 
- **portabilidad**: imagenes como user-service:latest son autocontenidas ejecutandose igual en dev, staging o prod, mientras que las VMs dependen de hipervisores y configuraciones especificas

* en los contenedores `user-service` y `order-service` son autonomos y ligeros lo que permite un despliegue rapido en Minikube



**Pasos de docker build -t user-service .:**

```Docker
# User-Service Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

- `FROM python:3.10-slim`: descarga imagen base es importante para establecer un entorno ligero y consistente
- `WORKDIR /app`: define  directorio de trabajo ayuda a tener rutas predecibles
- `COPY requirements.txt .`: copia dependencias es importante para instalar solo lo necesario
- `RUN pip install --no-cache-dir -r requirements.txt`: instala dependencias sin almacenar cache reduce tamaño de imagen
- `COPY app.py .`: copia codigo de la app  importante para incluir la logica del servicio
- `EXPOSE 8000`: documenta el puerto
- `CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]`: define  comando de arranque importante para ejecutar la app correctamente



### 2. **Optimizacion de Dockerfile**

**Analiza el Dockerfile de service-user y (diagrama de capas) justifica el orden de instrucciones.**

```Dockerfile
# User-Service Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```
**Capas:**
1. `FROM python:3.10-slim` : Base
2. `WORKDIR /app` : configuracion  directorio 
3. `COPY requirements.txt .` : copia archivo 
4. `RUN pip install --no-cache-dir -r requirements.txt` : instala fastAPI, uvicorn, pydantic
5. `COPY app.py .` : copia codigo
6. `EXPOSE 8000` : metadato
7. `CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]` : metadato 

**Justificacion del orden:**
1. `FROM` primero para establecer la base
2. `WORKDIR` antes de copiar para organizar archivos
3. `COPY requirements.txt` y `RUN pip install` antes de copiar el codigo para aprovechar el cache de Docker: cambios app.py no invalidan instalacion dependencias
4. `COPY  app.py` al final porque el codigo cambia
5. `EXPOSE` y `CMD` ultimos por ser metadatos

**Propon optimizaciones (por ejemplo, combinar instrucciones RUN, usar imagenes base mas ligeras) y detalla como mejorarian el tiempo de build o el tamaño de imagen**

* usar imagen base mas ligera se tendria que cambiaar a `python:3.10-alpine`
* multistage builds:
```Dockerfile
FROM python:3.10-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY app.py .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```
* tambie se podriaa especificar versiones en `requirements.txt`:
```c
fastapi==0.103.0
uvicorn==0.23.2
pydantic==2.4.2
```

### 3. **Redes y volumenes en un entorno real**

**3.1. Si tu microservicio necesitara persistir sesiones o logs de auditoria, ¿como montarias un volumen Docker?**

Se puede usar volumenes Docker que permite almacenar datos fuera del contenedor para que persistan despues de que el contenedor se elimine o reinicie  
**por ejemplo en service-user/app.py** si quiero guardar los usuarios creados:

- Primero creo un volumen en docker:
```Dockerfile
docker volume create user-service-data
```

- segundo, al desplegar debo montar el volumen en el contenedor:
```Dockerfile
docker run -v user-service-data:/app/data -p 8000:8000 user-service:latest
```

- despues actualizo el `service-user/app.py` algo asi:
```python
import os
import logging
logging.basicConfig(filename='/app/data/logs/auditoria.log', level=logging.INFO)
@app.post("/users/")
def create_user(user: User):
    logging.info(f"Usuari creado con id: {user.id}")
    users[user.id] = user.dict()
    return user
```

- y en kuberneetes modifico `k8s/user-deployment.yaml` para que incluya el volumen:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 2
  selector:
    matchLabels:
      app: user
  template:
    metadata:
      labels:
        app: user
    spec:
      containers:
      - name: user
        image: user-service:latest
        ports:
        - containerPort: 8000
        volumeMounts:
        - name: user-data
          mountPath: /app/data
      volumes:
      - name: user-data
        persistentVolumeClaim:
          claimName: user-service-pvc
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: user-service-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```
- Esto monta un volumen persistente en `app/data` para que guarde las sesiones y logs, estos datos persisten aun sise reinicia o elimina el contenedor

**3.2. En produccion, ¿que tipo de red usarias para comunicar los servicios user y order si estuviesen en distintos hosts, y por que?**

se usaria una red de cluster Kubernetes con servicios de tipo ClusterIP o LoadBalancer gestionada por un Container Network Interface

**En ClusterIP:**
```yml
apiVersion: v1
kind: Service
metadata:
  name: user-service
spec:
  selector:
    app: user
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
```
ClusterIP proporciona una direccion IP interna dentro del cluster para que los pods de `order-service` puedan comunicarse con `user-service` y viceversa usando el nombre del servicio `user-service` o `order-service` y esto funciona asi:
Kubernetes resuelve `user-service` a su IP interna mediante el DNS interno del cluster, permitiendo que `order-service` haga solicitudes HTTP a `http://user-service:80`

**LoadBalancer**
Si los servicios necesitan ser accesibles desde fuera del cluster cambiar el tipo de servicio a LoadBalancer
```yml
spec:
  type: LoadBalancer
  selector:
    app: user
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
```
Un LoadBalancer asigna una IP publica o un balanceador de carga en la nube esto es util para exponer APIs publicas sin embargo para comunicacion interna entre user-service y order-service, no es necesario

**CNI para comunicacion entre hosts**
asegurando baja latencia y seguridad mediante politicas de red

### 4. **Docker Compose para entornos de desarrollo**
**4.1. Diseña un docker-compose.yml que arranque:**

```yaml
version: '3.8'
services:
  user-service:
    build:
      context: ./service-user
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - user-data:/app/data
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    depends_on:
      - redis
    networks:
      - microservices-net

  order-service:
    build:
      context: ./service-order
      dockerfile: Dockerfile
    ports:
      - "8001:8001"
    volumes:
      - order-data:/app/data
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    depends_on:
      - redis
    networks:
      - microservices-net

  redis:
    image: redis:7.0
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    networks:
      - microservices-net

  redisinsight:
    image: redis/redisinsight:latest
    ports:
      - "5540:5540"
    depends_on:
      - redis
    networks:
      - microservices-net

volumes:
  user-data:
  order-data:
  redis-data:

networks:
  microservices-net:
    driver: bridge
```

* **user-service y order-service:**
    - build: usa los Dockerfile existentes en /service-user y ./service-order para construir las imagenes
    - ports: expone los puertos 8000 y 8001 para acceso local
    - volumes: Monta volumenes (user-data, order-data) para persistir datos como sesiones o logs
    - environment: Configura variables para conectar con Redis (REDIS_HOST=redis resuelve el nombre del servicio Redis en la red)
    - depends_on: Asegura que Redis este disponible antes de iniciar los servicios
    - networks: Conecta los servicios a una red comun microservices-net
+ **redis:**
    - usa la imagen oficial redis:7.0
    - expone el puerto 6379 para comunicacion interna y externa
    - monta un volumen redis-data para persistir la cache
    - conectado a la red microservices-net
* **redisinsight:**
    - usa la imagen oficial redis/redisinsight para una interfaz web de administracion de Redis
    - expone el puerto 5540 para acceso local localhost:5540
    - depende de redis para garantizar que la base de datos este lista


**4.2. Explica como Compose acelera el onboarding de nuevos desarrolladores y facilita simular entornos de staging locales.**

1.  **Onboarding de nuevos desarrolladores:** 

- **mas simple:** un solo comando docker-compose up inicia todos los servicios el de user-service, order-service, Redis, RedisInsight con sus dependencias configuradas los desarrolladores no necesitan instalar Python, Redis ni configurar entornos manualmente

- **consistencia:** el docker-compose.yml define imagenes, puertos, volumenes y redes, esto asegura que todos los desarrolladores trabajen en el mismo entorno y asi elimina el problema de "funciona en mi maquina"

- **documentacion implicita:** el archivo describe la arquitectura completa servicios, dependencias, redes, sirviendo como referencia clara para nuevos desarrolladores

- **entorno aislado:** la red microservices-net asegura que los serviccios se comuniquen entre si sin interferencias externas replicando un entorno real

2. **Simulacion de entornos de staging locales:**

- **replica el entorno:** docker compose simula la arquitectura de produccion microservicios + base de datos en una maquina local, permitiendo probar interacciones entre user-service, order-service y Redis sin necesidad de un cluster Kubernetesminikube ssh

- **persistencia de datos:** los volumenes (user-data, order-data, redis-data) permiten simular escenarios reales, como la persistencia de sesiones o datos de cache, cercanos a un entorno de staging.

- **facilita de pruebas:** los desarrolladores pueden modificar el codigo, reconstruir imagenes (docker-compose build) y probar cambios rapidamente y RedisInsight permite inspeccionar la cache visualmente, facilitando la depuracion

- **escalabilidad local:** aunque no tan robusto como Kubernetes  Compose permite ajustar configuraciones como replicas o recursos para simular comportamientos de staging
