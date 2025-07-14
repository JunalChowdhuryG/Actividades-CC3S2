# **Actividad 21: Patrones para módulos de infraestructura**



## **Fase 1: Exploración y análisis**


### **1. Singleton (singleton.py)**

```python
import threading
from datetime import datetime

class SingletonMeta(type):
    _instances: dict = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class ConfigSingleton(metaclass=SingletonMeta):
    def __init__(self, env_name: str):
        self.env_name = env_name
        self.settings: dict = {}
        self.created_at: str = datetime.utcnow().isoformat()
```
#### **Explica cómo SingletonMeta garantiza una sola instancia y el rol del lock.**

* `SingletonMeta` es una metaclase controla la creación de instancias de `ConfigSingleton`, `SingletonMeta` asegura que solo exista una instancia de `ConfigSingleton` la garantiaa de que solo una instancia es:
- el diccionario `_instances` guara toda las instancias que se han creaddo y utiliza la clase como indice ,   cuando se quiere intentar crear un instancia `__call__`  ese metodo verifica si la clase ya tiene una instancia en `_instances` en el caso que no exista se crea una nueva instancia usando `super().__call__(*args, **kwargs)` y lo almaceba en `_instances` pero en el caso que ya exista devuele la insatancia almacenada y asi evita crear una nueva instancia y tener duplicados

* el rol de `lock` en el caso de `threading.Lock` asegura que cuando se crea la instancia este sea seguro en entoornos multi hilos

* `with cls._lock` evita que  2 hilos creen instancias simultaneas esto evita romper el patron singleton sirve bastante en aplicaciones paralela o concurrentes 




