# **Actividad 1: Introduccion a DevOps**
`Junal Chowdhury Gomez`

## Indice
1. [**Lectura 1**](#Lectura-1)
    - [**Comprension y Reflexion**](#comprension-y-reflexion)
    - [**Preguntas de reflexion**](#preguntas-de-reflexion)
2. [**Lectura 2**](#lectura-2)
    - [**Preguntas de reflexion**](#preguntas-de-reflexion-1)

## **Lectura 1**

### **Comprension y Reflexion**
1. **Que es DevOps?**
    - DevOps es una metodologia que integra desarrollo y operaciones con el fin de agilizar el ciclo de vida del software, mejorar la calidad y minimizar la friccion y conflicto entre equipos
    - Representa un cambio cultural que busca alinear prioridades, mejjorar flujos de trabajo y eliminar barreras de organizacion

2. **Diferencias entre los equipos de desarrollo y operaciones en el pasado**
    - **Desarrollo:** Consistte en la creacion de nuevas funcionalidades
    - **Operaciones:** la prioridad era garantizar la estabilidad del sistema y la infraestructura
    - **Implementacion:** El codigo se transferiia desde desarrollo a operaciones sin una integracion fluida, lo que solia provocar problemas en la implementacion y el mantenimiento

3. **Principios fundamentales de DevOps (enfoque en el cliente, equipos autonomos y multifuncionales, mejora continua, automatizacion)**
    - enfoque en el cliente: Toda accion debe agregar valor al cliente, asegurando entregas rapidass y relevantes​
    - equipos autonomos y multifuncionales: Sin silos, con habilidades diversas y poder de decision​
    - mejora continua: Optimizacion constante de procesos y cultura de aprendizaje​
    - automatizacion: Minimiza errores, mejora eficiencia y facilita integracipn y entrega continuas

4. **Que NO es DevOps**
    - No son herramientas ni tecnologia por ejemplo: docker, git, github 
    - No sonn solo roles o individuos especificos​
    - No es solo un proceso por ejemplo Scrum

### **Preguntas de reflexion**


1. **¿Por que surgio la necesidad de DevOps en el desarrollo de software?**

    - Antes, el software era estatico por ejemplo videojuegos en discos o cartuchos,, y no requeria actualizaciones
    - Con la llegada de servidores y aplicaciones en la nube, el software comenzo a evolucionar continuamente
    - Se genero una brecha entre los equipos de desarrollo y operaciones:
        - Desarrollo buscabaa rapidez en la entrega de nuevas funciones
        - Operaciones priorizaba la estabilidad y seguridad del sistema
    - Esta friccion causaba retrasos en los lanzamientos y problemas al implementar software
    - DevOps surgio para integrar ambos equipos, reducir fricciones y permitir entregas mas rapidas y confiables​


2. **Explica como la falta de comunicacion y coordinacion entre los equipos de desarrollo y operaciones en el pasado llevo a la creacion de DevOps**

    - Desarrollo y operaciones trabajaban sin comunicacion efectivaa
    - Los desarrolladores entregaban codigo sin considerar el entorno de producioon
    - El equipo de operaciones recibia software incompleto o dificil de implementar
    - Esto provocaba:
        - Problemas en produccion
        - Desgaste y frustracion en los equipos
        - Procesos lentos e ineficientes
    - DevOps nacio para romper estos siloss, fomentar la colaboracion y mejorar la integracion entre ambos equipos​

3. **Describe como el principio de mejora continua impacta tanto en los aspectos tecnicos como en los culturales de una organizacion**

    - Impacto tecnico:
        - Mejora la confiabilidad, adaptabilidad y eficiencia del software
        - Optimiza procesos de entrega y monitoreo de metricas clave
        - Permite ajustes rapidos basados en datos de rendimiento
    - Impacto cultural:
        - Fomenta la colaboracion entre equipos
        - Impulsa una cultura de aprendizaje y experimentacion
        - Ayuda a desmantelar silos organizzacionales
  


4. **¿Que significa que DevOps no se trata solo de herramientas, individuos o procesos?**
    - no basta con usar tecnologias como docker, github o CI/CD
    - no se trata solo de contratar o formar "equipos DevOps"
    - no es simplemente adoptar procesos agiles como Scrum
    - DevOps requiere:
        - Un cambio cultural dentro de la organizacion
        - Colaboracioon efectiva entre desarrollo y operaciones
        - Automatizacion estrategica para optimizar procesos sin generar burocracia innecesaria
    - sin estos elemento, las herramientas y metodologias pueden generar mas carga operativa en lugar de mejorar la eficiencia​


5. **Segun el texto, ¿como contribuyen los equipos autonomos y multifuncionales a una implementacion exitosa de DevOps?**

    - Eliminar barreras entre desarrollo, operaciones y QA
    - Formar equipos con habilidades diversas como desarrollo, pruebas, despliegue, diseño
    - Agilizar la toma de decisiones sin depender de multiples aprobaciones
    - Evitar cuellos de botella y tiempos de espera en la entrega de software
    - Fomentar la responsabilidad y la colaboracion dentro del equipo
    - Permitir que el software se desarrolle, implemente y mantenga de manera eficiente y sin fricciones​


## **Lectura 2**

### **Lectura y Analisis**
-  **DevSecOps**: 
    - enfoque de desarroollo de software que integra seguridad en el ciclo de vida
    - automatiza y garantiza la seguridad desde el inicio 


### **Preguntas de reflexion**

1. **¿Que significa "desplazar a la izquierda" en el contexto de DevSecOps y por que es importante?**
    - se refiere a la integracion temprana de la seguridad en el ciclo de vida del desarrollo de software tambien
    - permite detectar y corregir vulnerabilidades desde las fases iniciales reduciendo costos y riesgos
    - mminimiza retrasos en los lanzamientos al evitar que los problemas de seguridad se descubran tarde

2. **Explica como IaC mejora la consistencia y escalabilidad en la gestion de infraestructuras.**

    - elimina la configuracion manual , reduciendo errores humanos.
    - define el estado de la infraestructura en codigo, asegurando entornos replicables.
    - permite automatizar despliegues , haciendo que la infraestructura sea escalable y eficiente.
    - facilita la gestion de sistemas complejos sin depender de documentacion manual​

3. **¿Cual es la diferencia entre monitoreo y observabilidad? ¿Por que es crucial la observabilidad en sistemas complejos?**

    - **monitoreo**: Se basa en reglas predefinidas y metricas establecidas, enfocandose en detectar problemas conocidos
    - **observabilidad**: Proporciona una visison profunda del sistema, permitiendo diagnosticar problemas sin necesidad de conocerlos previamente
    - **Importancia en sistemas complejos**: Permite comprender la interacion entre multiples componentes, facilitando la identificacion de cuellos de botella y optimizacion del rendimiento​

4. **¿Como puede la experiencia del desarrollador impactar el exito de DevOps en una organizacion?**

    - Un entorno de trabajo eficiente y colaborativo y aumenta la productividad y satisfaccion de los desarrolladores
    - Reduce silos y mejora la comunicacion dentro de los equipos
    - Facilita la implementacion de buenas practicas DevvOps al promover herramientas y flujos de trabajo optimizados
    - Impacta directamente en la calidad y velocidad del desarrollo de software​


5. **Describe como InnerSource puede ayudar a reducir silos dentro de una organizacion.**
    - Fomenta la colaboracion abierta entre equipos mediante la contribucion compartida a proyectos internos
    - Promueve la transparencia en la toma de decisiones y gestion de codigp
    - Facilita la mentoria y el intercambio de conocimientos, empoderando a los desarrolladores
    - Reduce la dependencia de equipos especificos al permitir que cualquier desarrollador contribuya a diferentes proyectos​

6. **¿Que rol juega la ingenieria de plataformas en mejorar la eficiencia y la experiencia del desarrollador?**

    - Automatiza la infraestructura y operaciones, reduciendo la carga cognitiva de los desarrolladores
    - Proporciona plataformas internas con herramientas y servicios reutilizables
    - facilita el autoservicio, permitiendo a los desarrolladores centrarse en la entrega de valor sin preocuparse por la infraestructura
    - mejora la eficiencia operativa mediante la integracion de CI/CD y IaC
