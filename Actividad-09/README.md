
# **Actividad 9: Red-Green-Refactor**

## **Ejercicio**
Desarrolla las 6 iteraciones de Desarrollo Guiado por Pruebas (TDD) (Red-Green-Refactor) aplicadas a la clase UserManager, incluyendo casos de mocks, stubs, fakes, spies e inyección de dependencias. Cada iteración presenta un escenario diferente para ilustrar cómo podrías usar estas técnicas.

### **Historial de Commits del proceso Red-Green-Refactor con 6 iteraciones**

![](img/A9-git-log.png)

### **Iteración 1: Agregar usuario (Básico)**

#### **Paso 1 (Red): Escribimos la primera prueba**
![](img/A9-I1-RED.png)

#### **Paso 2 (Green): Implementamos lo mínimo para que pase la prueba**
![](img/A9-I1-GREEN.png)

### **Iteración 2: Autenticación de usuario (Introducción de una dependencia para Hashing)**

#### **Paso 1 (Red): Escribimos la prueba**
![](img/A9-I2-RED.png)

#### **Paso 2 (Green): Implementamos la funcionalidad y la DI**
![](img/A9-I2-GREEN.png)



### **Iteración 3: Uso de un Mock para verificar llamadas (Spy / Mock)**

#### **Paso 1 (Red): Escribimos la prueba de "espionaje"**
![](img/A9-I3-RED.png)

#### **Paso 2 (Green): Probar que todo pasa**
Realmente, nuestro código ya llama a `hash_service.hash`. Si ejecutamos pytest, la prueba debería pasar de inmediato, pues la implementación actual ya cumple la expectativa.



### **Iteración 4: Excepción al agregar usuario existente (Stubs/más pruebas negativas)**

#### **Paso 1 (Red): Prueba**
![](img/A9-I4-RED.png)

#### **Paso 2 (Green)**
Nuestra lógica ya lanza `UserAlreadyExistsError` si `user_exists` devuelve `True`. Así que la prueba debería pasar sin modificar el código.



### **Iteración 5: Agregar un "Fake" repositorio de datos (Inyección de Dependencias)**

#### **Paso 1 (Red): Nueva prueba**
![](img/A9-I5-RED.png)

#### **Paso 2 (Green): Implementación**
![](img/A9-I5-GREEN.png)


### **Iteración 6: Introducir un “Spy” de notificaciones (Envío de correo)**

#### **Paso 1 (Red): Prueba**
![](img/A9-I6-RED.png)

#### **Paso 2 (Green): Implementamos la llamada al servicio de correo**
![](img/A9-I6-GREEN.png)
