# **Actividad 3: Computacion en la nube**

## **A. Cuestionario**


### **1. Motivaciones para la nube**

* **(a)¿Que problemas o limitaciones existian antes del surgimiento de la computacion en la nube y como los soluciono la centralizacion de servidores en data centers?**

    * Problemas antess de  la nube:

        - ifraestructura local de alto costos (hardware y mantenimiento)
        - Dificultad para escalar segun lo que requeria
        - necesidad de sobreaprovisionamiento para picos de carga
        - Problemas de disponibilidad y fallos en servidores locales

    * Solucion con data centers centralizados:

        - Acceso a recursos bajo demanda
        - reduccion de costos operativos
        - Mayor confiabilidad y escalabilidad
        - administracion simplificada de la infraestructura


* **(b) ¿Por que se habla de “The Power Wall” y como influyo la aparicion de procesadores multi-core en la evolucion hacia la nube?**

    * “The Power Wall”: limitacion en el aumento de la velocidad de procesadores debido al consumo energetico y la disipacion de calor
    * Solucion: Procesadores multi-core permiten ejecutar multiples tareas en paralelo sin aumentar el consumo de energia excesivamente

    * Impacto en la nube:

        - mejora en la eficiencia del procesamiento
        - habilitacion de la virtualizacion y la ejecucion de multiples instancias en servidores
        - aumento en la capacidad de procesamiento de data centers

### **2. Clusters y load balancing**
* [Fuente: AWS.amazon](https://aws.amazon.com/what-is/load-balancing/)
* **load balancers**: Es el metodo de distribuir el trafico de red de manera equitativa en un conjunto de recursos que admiten una aplicacion
* **(a) Explica como la necesidad de atender grandes volumenes de trafico en sitios web condujo a la adopcion de clusteres y balanceadores de carga.**
    * Problema:
        - aumento del trafico en sitios web puede sobrecargar un solo servidor
        - Riesgo de caida del servicio y degradacion del rendimiento
    * solucion:
        - uso de clusteres (conjunto de servidores trabajando juntos)
        - Implementacion de balanceadores de carga que distribuyen el trafico entre los servidores
        - Mejora en escalabilidad, disponibilidad y eficiencia


* **(b) Describe un ejemplo practico de como un desarrollador de software puede beneficiarse del uso de load balancers para una aplicacion web.**
    * **Ejemplo practico:**
        - un desarrollador tiene una aplicacion web con alto trafico.
        - implementa un load balancer (por ejemplo, AWS Elastic Load Balancer).

    * **Beneficios:**
        - Distribuye el trafico entre multiples servidores
        - asegura alta disponibilidad (si un servidor fallla, el trafico se redirige)
        - mejora la esscalabilidad automatica de la aplicacion

### **3. Elastic computing** 
* [Fuente: Azure Microsfoft](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-elastic-computing)
* **(a) Define con tus propias palabras el concepto de Elastic Computing.**
    *  es la capacidad para aumentar o reducir recursos de computo segun requiear la demanda
    * Optimiza costos y mejora el rendimiento en la nube
    * permite Alas equipos y empresas adaptarse a cambio de carga sin intervencion humana
* **(b) ¿Por que la virtualizacion es una pieza clave para la elasticidad en la nube?**
    * esto permite la creacion de de maquinas virutales en servidores fisicos
    * Tambien facilita la a asignacion y liberacion de recursos
    * Aumenta  la flexibilidad sin necesidad de comprar equipos de hardware adicional
* **(c) Menciona un escenario donde, desde la perspectiva de desarrollo, seria muy dificil escalar la infraestructura sin un entorno elastico.**
    * Escenario: Una tienda en linea en  Black Friday, esto causa un aumento de usuarios
    * Sin elasticidad: tendria que comprar y configurar seervidoers fisicos con anticipacion
    * Con elasticidad:: aumentan la flexibilidad sin tener lanecesidad de comprar harware adicional

### **4. Modelos de servicio (IaaS, PaaS, SaaS, DaaS)** 

* Fuentes:
    - [Citrix DaaS vs. SaaS vs. PaaS vs. IaaS](https://www.citrix.com/blogs/2022/01/20/saas-vs-paas-vs-iaas-vs-daas/)
    - [IBM: Iaas, Paas y Saas](https://www.ibm.com/think/topics/iaas-paas-saas)

* **(a) Diferencia cada uno de estos modelos. ¿En que casos un desarrollador optaria por PaaS en lugar de IaaS?** 

    | Modelo  | Descripcion | Ejemplos |
    |---------|------------|----------|
    | **IaaS** (Infraestructura como Servicio) | proporciona hardware virtualizado como servidores, almacenamiento | AWS EC2, Google Compute Engine |
    | **PaaS** (Plataforma como Servicio) | proporciona herrramientas y entornos gestionados para desarrolllo y despliegue | AWS Elastic Beanstalk, Google App Engine |
    | **SaaS** (Software como Servicio) | aplicaciones listas para usar desde la nube | GoogleDocs, Dropbox |
    | **DaaS** (Desktop como Servicio) | escritorios virtuales accesibles desde la nube | Amazon Workspaces, Citrix Virtual Apps |

    * ¿Cuando elegir PaaS sobre IaaS?
        * Cuando el desarrollador quiere enfocarse en el codigo sin preocuparse por la infraestructura
        * Cuando se necesita escalabilidad automatica y administracion simplificada

* **(b) Enumera tres ejemplos concretos de proveedores o herramientas que correspondan a cada tipo de servicio.**

    | Modelo  | Ejemplos |
    |---------|------------|
    | **IaaS** | AWS EC2, Google Compute Engine, Azure Virtual Machines |
    | **PaaS** | AWS Elastic Beanstalk, Azure App Service, Google App Engine |
    | **SaaS** | Google Docs, Salesforce, Dropbox |
    | **DaaS** | Amazon WorkSpaces, Citrix Virtual Apps, Microsoft Azure Virtual Desktop |


### **5. Tipos de nubes (Publica, Privada, Hibrida, Multi-Cloud)**  
* **(a) ¿Cuales son las ventajas de implementar una nube privada para una organizacion grande?**  
    * se tiene un mayor control sobre la infraestructura y los datos
    * tambien se tiene un mejor cumplimiento con regulaciones de seguridad
    * tambien optimizacion del rendimiento y costos para cargas de trabajo especificas

* **(b) ¿Por que una empresa podria verse afectada por el “provider lock-in”?** 
    * Fuentes:
        * [Arsys: vendor lock-in](https://www.arsys.es/blog/que-es-vendor-lock-in-que-tipos-existen-y-como-se-puede-evitar-esta-situacion)

    * **vendor lock-in:** Dificultad para migrar a otro proveedor de nube debido a dependencia tecnologica.
    * Problemas
        * pueden producir altos costos de migracion
        * tambien pueden producirse problemas de compatibilidad con otras plataformas
        * otro problema que se puede producir es la dependencia de herramientas y servicios especificos de un proveedor

* **(c) ¿Que rol juegan los “hyperscalers” en el ecosistema de la nube?**
    * [RedHat: what-is-a-hyperscaler](https://www.redhat.com/es/topics/cloud-computing/what-is-a-hyperscaler)
    * Son grandes proveedores de infraestructura en la nube como Amazon Web Services, Google Cloud,Microsoft Azure, IBM Cloud y Alibaba Cloud
    * Permmiten acceso a recursos escalables y de alta disponibilidad
    * Facilitan el desarrolllo e implementacion de apliccaciones globales


## **B. Actividades de investigacion y aplicacion**

### **1. Estudio de casos**
* **Fuentes:**
    * [Netflix: Netflix se muda a la nube](https://about.netflix.com/es/news/completing-the-netflix-cloud-migration)
    * [LinkenIn: netflixs story migration aws nilay saraf](https://www.linkedin.com/pulse/netflixs-story-migration-aws-nilay-saraf)
    * [AWS: Estudio de caso de migracion Airbnb](https://aws.amazon.com/es/solutions/case-studies/airbnb-case-study/)

#### **Netflix**
En base a [Netflix](https://about.netflix.com/es/news/completing-the-netflix-cloud-migration) y [LinkenIn](https://www.linkedin.com/pulse/netflixs-story-migration-aws-nilay-saraf)
* **Motivaciones para la migracion:**
    * Alta demanda de procesamiento y almacenamiento debido al crecimiento global
    * Necesidad de escalabilidad para manejar picos de trafico (por ejemplo, estrenos de series populares)
    * Mantenimiento costosos y complejos de data centers fisicos
* **Beneficios obtenidos:**
    * Escalalabilidad dinamica: Puede aumentar o reducir servidores automaticamente segun la demanda
    * Reduccion de costos: Eliminacion de gastos en infraestructura fisica
    * Alta disponibilidad: Uso de multiples regiones en la nube para evitar caidas del servicio
* **Desafios enfrentados:**
    * Seguridad y proteccion de datos: Garantizar que la informacion de usuarios este protegida
    * Migracion sin interrupciones: Mantener el servicio activo mientras se realizaba la transicion a la nube
    * Optimizacion de costos: Asegurar que el gasto en la nube no se disparara con el crecimiento
* **Solucion:** Netflix adopto AWS (Amazon Web Services) y diseño su infraestructura para ser completamente basada en la nube, utilizando herramientas como AWS Lambda y Amazon S3.

#### **Airbnb**
En base a [AWS](https://aws.amazon.com/es/solutions/case-studies/airbnb-case-study/)
* **Motivaciones para la migracion:**
    * Rapido crecimiento internacional y la necesidad de manejar grandes volumenes de trafico.
    * Reduccion de costos en infraestructura fisica.
    * Necesidad de optimizar el rendimiento de su plataforma en diferentes regiones.
* **Beneficios obtenidos:**
    * mayor flexibilidad: Puede escalar servidores segun la demanda de reservas.
    * mejorar rendimiento: Reduccion en los tiempos de respuesta de su plataforma.
    * Menor costo de mantenimiento: Eliminacion de servidores fisicos y gastos de mantenimiento.
* **Desafios enfrentados:**
    * Seguridad y privacidad: Manejo de datos personales de usuarios en diferentes paises.
    * Cumplimiento normativo: Cumplir con regulaciones como GDPR en Europa.
    * Gestion eficiente de recursos en la nube: Evitar pagar mas de lo necesario por servicios en la nube.
* **Solucion:** Airbnb migro su infraestructura a AWS, utilizando servicios como Amazon RDS, S3 y EC2 para gestionar su plataforma de manera eficiente.


### **2. Comparativa de modelos de servicio**
* Fuente:
    - [Microsoft: Responsabilidad compartida en la nube](https://learn.microsoft.com/es-es/azure/security/fundamentals/shared-responsibility)


| **Responsabilidad**                | **IaaS** (Infraestructura como Servicio) | **PaaS** (Plataforma como Servicio) | **SaaS** (Software como Servicio) | **On-Premise** (Infraestructura local) |
|-------------------------------------|-----------------------------------------|-------------------------------------|-----------------------------------|-----------------------------------|
| **Informacion y datos**            |  Cliente                              |  Cliente                          |  Cliente                        |  Cliente                        |
| **Dispositivos (Moviles y PCs)**    |  Cliente                              |  Cliente                          |  Cliente                        |  Cliente                        |
| **Cuentas e identidades**          |  Cliente                              |  Cliente                          |  Cliente                        |  Cliente                        |
| **Infraestructura de identidades y directorios** |  Cliente |  Compartida (Cliente + Proveedor) |  Proveedor |  Cliente |
| **Aplicaciones**                   |  Cliente                              |  Cliente                          |  Proveedor                      |  Cliente                        |
| **Controles de red**               |  Cliente                              |  Compartida (Cliente + Proveedor) |  Proveedor                      |  Cliente                        |
| **Sistema operativo**              |  Cliente                              |  Proveedor                        |  Proveedor                      |  Cliente                        |
| **Hosts fisicos**                  |  Proveedor                            |  Proveedor                        |  Proveedor                      |  Cliente                        |
| **Red fisica**                     |  Proveedor                            |  Proveedor                        |  Proveedor                      |  Cliente                        |
| **Data center fisico**             |  Proveedor                            |  Proveedor                        |  Proveedor                      |  Cliente                        |
| **Instalacion del sistema operativo** |  Cliente                           |  Proveedor                        |  Proveedor                      |  Cliente                        |
| **Despliegue de aplicaciones**     |  Cliente                              |  Cliente                          |  Proveedor                      |  Cliente                        |
| **Escalado automatico**            |  Cliente o Proveedor si se configura |  Proveedor                        |  Proveedor                      |  No disponible                  |
| **Parches de seguridad**           |  Cliente                              |  Proveedor                        |  Proveedor                      |  Cliente                        |

### **3. Armar una estrategia multi-cloud o hibrida**

* **Fuente:**
    * [Oracle: Multicloud](https://www.oracle.com/cloud/multicloud/what-is-multicloud/)
    * [Cloud folio3: Multi-Cloud Migration](https://cloud.folio3.com/blog/multi-cloud-migration/)
En base a la fuente: [Cloud folio3: Multi-Cloud Migration](https://cloud.folio3.com/blog/multi-cloud-migration/)



#### **1. Evaluacion y planificacion**  
Primero debemos evluar
- **Tipos de cargas de trabajo** (monoliticas, microservicios, bases de datos, etc.)  
- **Dependencias entre aplicaciones** y su latencia
- **Costos de operacion en el nuevo proveedor de nube**
- **Seguridad y cumplimiento** (GDPR, ISO 27001, etc.)

---

#### **2. Arquitectura de la estrategia Multi-Cloud**  

**Distribucion de cargas de trabajo**  
- **Data Center On-Premises**: Mantendria servicios criticos y almacenamiento de datos sensibles
- **Proveedor de nube 1 (actual)**: Seguiria operando con la mitad de las aplicaciones y bases de datos primarias
- **Proveedor de nube 2 (nuevo)**: Recibiria la otra mitad de las aplicaciones y una replica de la base de datos

**Base de datos**  
- Utilizaria **una base de datos distribuida** por ejemplo, PostgreSQL con replicacion en la nube o Google Spanner/Aurora Multi-Region.  
- **Replica activa en el segundo proveedor** con sincronizacion de datos en tiempo real.  
- **Estrategia de failover** automatica en caso de caida de un proveedor.  

**Configuracion de red**  
- **VPN Site-to-Site o SD-WAN** para conectar el data center con ambas nubes.  
- **Balanceador de carga global** (ej. AWS Global Accelerator o Cloudflare Load Balancer) para distribuir trafico dinamicamente.  
- **Enrutamiento BGP** con redundancia para asegurar conectividad.  
- **IAM centralizado** para que los accesos sean consistentes entre ambos proveedores.  

---

#### **3. Plan de contingencia en caso de falla**  

- **Si un proveeedor falla**, el balanceador global redirige trafico al otro  
- **Base de datos en modo read-replica** en la segunda nube, con failover automatico
- **Backups automaticos y snapshot cross-cloud** en ambas nubes para recuperacion
- **Monitorizacion proactiva** con herramientas como Prometheus, Datadog o CloudWatch para alertas tempranas

### **4. Debate sobre costos**

- Definiciones: 
    - CAPEX (Capital Expenditure): Gasto de capital en activos fisicos como servidores, centros de datos y redes. Se paga por adelantado y es una inversion a largo plazo.
    - OPEX (Operational Expenditure): Gasto operativo recurrente, como costos de suscripcion en la nube, mantenimiento y consumo de recursos. Se paga periodicamente (mensual/anual).

* Fuentes:
    - [Microsoft: ¿Que son las nubes publica, privada e hibrida?](https://azure.microsoft.com/es-es/resources/cloud-computing-dictionary/what-are-private-public-hybrid-clouds)
    - [Cloudvisor: Choosing the Right Cloud Deployment Model: Public, Private, Hybrid, or Multi-Cloud?](https://cloudvisor.co/blog/cloud-deployment-models-public-private-hybrid-or-multi-cloud/) 
    - [Telefonica: Diferencias entre nube publica, nube privada, nube hibrida y multicloud](https://www.telefonica.com/es/sala-comunicacion/blog/diferencias-nube-publica-nube-privada-nube-hibrida-multicloud/)

    | **Tipo Nube**  | **Pross** | **Contras** |
    |-------------------|---------|------------|
    | **Nube Publica** | - Bajo CAPEX, alto OPEX: No requiere inversion inicial en hardware, pagas por uso <br>  - Alta escalabilidad: Recursos disponibles bajo demanda <br>   - Cumplimiento simplificado: Grandes proveedores ya cumplen con normativas (GDPR, HIPAA, etc.) |  - Costos crecientes: A largo plazo, el pago por consumo puede volverse costoso <br>  - Vendor Lock-in: Migrar a otro proveedor puede ser complejo y costoso. <br>   - Menos control sobre datos: Dependencia de la seguridad del proveedor. |
    | **Nube privada** | - Mayor control y seguridad: Ideal para datos sensibles y cumplimiento estricto. <br> -  Costos predecibles: Inversion inicial alta (CAPEX), pero costos a largo plazo mas estables. <br> -  Personalizacion total: Hardware y software ajustados a necesidades especificas. |  - Alto CAPEX: Inversion en infraestructura, mantenimiento y personal especializado. <br> -   Escalabilidad limitada: Crecer implica comprar mas hardware. <br> -   Mayor carga operativa: Se requiere administracion interna 24/7. |
    | **Nube Hiibrida** | - Balance entre costo y control: Datos sensibles en privado, cargas flexibles en publico. <br> -  Escalabilidad: Se puede extender capacidad con nube publica sin grandes inversiones. <br> -  Cumplimiento mas facil: Se pueden cumplir normativas manteniendo datos criticos en on-premises. |  - Costos operativos elevados: Administrar multiples entornos es complejo. <br> -   Integracion y compatibilidad: Necesidad de herramientas como VPN, SD-WAN y balanceo de carga. <br> -   Personal especializado: Se requiere talento en ambas infraestructuras. |
    | **Multi - Cloud** | - Evita dependencia de un solo proveedor: Mayor resiliencia y negociacion de costos. <br> -  Optimizacion de costos: Se pueden aprovechar precios y caracteristicas de cada proveedor. <br> -  Redundancia mejorada: Reduccion del riesgo de caidas de servicio. |  - Mayor complejidad: Configuracion y administracion de varias nubes requiere experiencia. <br> -   Costos ocultos: Trafico entre nubes, sincronizacion de datos y licencias pueden aumentar costos. <br> -   Dificultad en cumplimiento: Normativas varian segun el proveedor y ubicacion de datos. |



