# **Actividad 6: Rebase, Cherry-Pick y CI/CD en un entorno ágil**

## **Parte 1: git rebase para mantener un historial lineal**

1. Crea un nuevo repositorio Git y dos ramas, main y new-feature:
```shell
$ mkdir prueba-git-rebase
$ cd prueba-git-rebase
$ git init
$ echo "# Mi Proyecto de Rebase" > README.md
$ git add README.md
$ git commit -m "Commit inicial en main"
```
![](img/E1-1-Crear-repositorio-commit-main.png)


2. Crea y cambia a la rama new-feature:
```shell
$ git checkout -b new-feature
$ echo "Esta es una nueva característica." > NewFeature.md
$ git add NewFeature.md
$ git commit -m "Agregar nueva característica"
```
![](img/E1-2-commit-new-feature.png)


3. **Pregunta:** Presenta el historial de ramas obtenida hasta el momento.
![](img/E1-3-historial.png)



4. Ahora, digamos que se han agregado nuevos commits a main mientras trabajabas en new-feature:
```shell
# Cambiar de nuevo a 'main' y agregar nuevos commits
$ git checkout main
$ echo "Updates to the project." >> Updates.md
$ git add Updates.md
$ git commit -m "Update main"
```
![](img/E1-4-commit-main.png)


5. Tu gráfico de commits ahora diverge (comprueba esto)
![](img/E1-5-log-2.png)


6. **Tarea:** Realiza el rebase de new-feature sobre main con los siguientes comandos:
```shell
$ git checkout new-feature
$ git rebase main
```
![](img/E1-6-rebase-main.png)

**Revisión:**
7. Después de realizar el rebase, visualiza el historial de commits con:
```shell
$ git log --graph –oneline
```
![](img/E1-7-log-3.png)

8. Momento de fusionar y completar el proceso de git rebase:
```shell
# Cambiar a 'main' y realizar una fusión fast-forward
$ git checkout main
$ git merge new-feature
```
![](img/E1-8-merge-new-feature.png)
- Cuando se realiza una fusión fast-forward, las HEADs de las ramas main y new-feature serán los commits correspondientes.


## **Parte 2: git cherry-pick para la integración selectiva de commit**

1. Iniciamos el repositorio
![](img/E2-1-iniciar-repositorio.png)

2. Hacemos un commit del archivo `README` en la rama `main`
![](img/E2-2-commit-readme.png)

3. Cambiamos  a la rama `add-base-documents`
![](img/E2-3-cambio-rama-add-base-documents.png)

4. Hacemos un commit del archivo `CONTRIBUING` en la rama `add-base-documents`
![](img/E2-4-commit-contribuing.png)

5. Hacemos un commit del archivo `LICENSE`
![](img/E2-5-commit-license.png)

6. Verificamos el historial
![](img/E2-6-git-log.png)

7. Hacemos el `cherry-pick` al hash del commit del archivo `CONTRIBUING`
![](img/E2-7-cherry-pick.png)

8. Visualizamos y comprovamos la ejcucion del `cherry-pick` 
![](img/E2-8-vizualizacion-detallada.png)

**Preguntas de discusión:**

- ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge?
    - Rebase reescribe el historial y se sobrepone los commits sobre cierto punto base como si se huberan creados despues de el, esto hace que elhistorial sea mas facil de leer sin tantas bifurcaciones

- ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?
    - si se hace un `rebase` en ramas compartidas y fuerzas un `push` los demas colaboradores podrian tener un historial distinto, ya que reescribistes el historial

- ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?
    - `merge`
        - **Que hace?:** fusiona todo el historial en una rama
        - **Se usa, cuando:** quieres integrar todo
    - `cherry-pick`
        - **Que hace?:** trae commits especificos 
        - **Se usa, cuando:** solo quieres ciertas partes especificas

- ¿Por qué es importante evitar hacer rebase en ramas públicas?
    - ya que `rebase` reescribe el historial, los demas colaboradores podrian tener un historial distinto y producirian conflictos


## **Ejercicios teóricos**

### **1. Diferencias entre git merge y git rebase**
**Pregunta: Explica la diferencia entre git merge y git rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum.**
- **Merge**
    - sin modificar el historial combina el historial de 2 ramas haciendo un commit de merge
    - la mayor ventaja es que mantiene historial completo con bifurcaciones, y esto es util para auditar la historia del proyecto
    - la desventaja que puede tener es que con tantos merge el historial puede ser confuso
- **Rebase**
    - reescribe el historial, superponiendo commits sobre otra base, y no crea un commit de merge
    - la ventaja es que  mantiene un historial limpio y lineal, lo cual hace que sea de facil de leer
    - la desventaja es que si estas en un entorno de colaboracion, puede causar problemas si se comparte ramas entre los programadores
- **El uso en SCRUM**
    Es frecuente en SCRUM utilizar `merge` para integrar ramas de sprint a la main, y el `rebase` es utilizado localmente para tener un historial claro y limpio antes de subir cambios

### **2. Relación entre git rebase y DevOps**
**Pregunta: ¿Cómo crees que el uso de git rebase ayuda a mejorar las prácticas de DevOps, especialmente en la implementación continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.**
- el `rebase` reescribe el historial de manera que los commits aparecen como si se hubieran hecho en la `main`, esto ayuda a tener un historial claro y limpio
- cuando se tiene un historial lineal, hay menos problemas de conflictos de fusion y eso ayuda a que los pipeline de CI puedan ejecutarse con facilidad
- Al tener un historial limpio y lineal, para los casos de falla en produccion sera mas facil identificar con exactitud en que punto del desrrollo se produjo el fallo


### **3. Impacto del git cherry-pick en un equipo Scrum**
**Pregunta: Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que solo algunos commits específicos de la rama de una funcionalidad deben aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este caso? Explica los beneficios y posibles complicaciones.**

- `cherry-pick` permite seleccionar commits especificos de una rama y aplicarlos a otra rama sin necesidad de mezclar toda la rama
- Los Beneficios son:
    - Es muy flexible para liberar lo necesario
    - Gracias al cherry-pick evitas hacer `merge` a cambios que aun no estan listos o que presentanb problemas
    - Para Scrum es beneficioso cuando hay entregas parciales o despliegues de imprevistos o urgentes
- las complicaciones que pueden suceder:
    - Es posible que suceda erores humanos como  equivocarse al seleccionar commits
    - duplica  el historial si se hace un merge de la rama completa 
    - puede que genere conflictos si los commits dependen de otros que no estan seleccionados

## **Ejercicios prácticos**

### **1. Simulación de un flujo de trabajo Scrum con git rebase y git merge**
1. Inicializar repositorio y hacer commit en main
![](img/E3-1-INICIAR-REPO-COMMIT-MAIN.png)

2. Crear rama feature y hacer un commit
![](img/E3-2-COMMIT-FEATURE.png)

3. Volver a main y hacer un nuevo commit
![](img/E3-3-COMMIT-MAIN.png)

4. Rebase de feature sobre main
![](img/E3-4-REBASE-FEATURE-MAIN.png)

5. Fusión fast-forward
![](img/E3-5-FF.png)

**Preguntas**
- **¿Qué sucede con el historial de commits después del rebase?**
    - El historial queda completamente lineal
- **¿Cuándo aplicarías una fusión fast-forward en un proyecto ágil?**
    - Si quiero manterner histtorial limpio y lineal
    - cuando hago un rebase en un `feature` sobre `main` antes de hacer merge
    - cuando quiero hacer un merge y no hay conflicto sin necesidad de un commit de merge

### **2. Cherry-pick para integración selectiva en un pipeline CI/CD**

1. Crear el repositorio e inicializar rama main
![](img/E4-1-INICIAR-REPO.png)

2. Crear rama feature y hacer varios commits
![](img/E4-2.png)

3. Ver los hashes de los commits
![](img/E4-3.png)

4. Hacer cherry-pick de los commits seleccionados
Supongamos que solo quieres mover la primera característica a producción por ahora:
![](img/E4-4.png)

5. Verifica que los commits ahora están en main
![](img/E4-5.png)

**Preguntas**
- **¿Cómo utilizarías cherry-pick en un pipeline de CI/CD para mover solo ciertos cambios listos a producción?**
    - 
- **¿Qué ventajas ofrece cherry-pick en un flujo de trabajo de DevOps?**
    - Me permite seleccionar que cambios en especifico se van a produccion
    - solo se registran commits relevantes en `branch` como la main
    - Es muy ventajoso cuando se implementa en pipeline automatizados para entregas controladas
 