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




