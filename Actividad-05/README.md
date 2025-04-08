# **Actividad 5: Explorando diferentes formas de fusionar en Git**

## **Ejemplos**
### **1. Fusión Fast-forward (git merge --ff)**
1. Crear un nuevo repositorio

    ```shell
    $ mkdir prueba-fast-forward-merge
    $ cd prueba-fast-forward-merge
    $ git init
    ```
    ![](img/E1-crear-directorio.png)


2. Agregar un archivo inicial en la rama principal (main)

    ```shell
    $ echo "# Mi Proyecto" > README.md
    $ git add README.md
    $ git commit -m "Commit inicial en main"
    ```

    - Crea el archivo
    ![](img/E1-crear-archivo-readme.png)

    - Se hace el primer `git commit`
    ![](img/E1-primer-commit.png)


3. Crear y cambiar a una nueva rama 'add-description'

    - Añade modificacion al `README.md` en la rama `add-description`
    ```shell
    $ git checkout -b add-description
    $ echo "Este proyecto es un ejemplo de cómo usar Git." >> README.md
    ```
    ![](img/E1-rama-fast-forward.png)


4. Se comitea los cambios
    ```shell
    $ echo "Este proyecto es un ejemplo de cómo usar Git." >> README.md
    $ git add README.md
    $ git commit -m "Agregar descripción al README.md"
    ```
    ![](img/E1-segundo-commit.png)

5. Cambiar de vuelta a la rama 'main' y realizar la fusión fast-forward
    ```shell
    $ git checkout main
    $ git merge add-description

    # Ver el historial lineal
    $ git log --graph --oneline
    ```
    ![](img/E1-rama-fast-forward.png)

- **Pregunta:** Muestra la estructura de commits resultante.
    ![](img/E1-log-graph.png)

### **2. Fusión No-fast-forward (git merge --no-ff)**

1. Creamos el repositorio
![](img/E2-crear-repositorio.png)

2. Agregar un archivo inicial en la rama principal (main)
![](img/E2-primer-commit.png)

3. Crear y cambiar a una nueva rama `add-feature`
![](img/E2-crear-rama.png)

4. Hacer cambios en la nueva rama y comitearlos
![](img/E2-segundo-commit.png)

5. Cambiar de vuelta a la rama 'main' y realizar una fusión no-fast-forward
![](img/E2-merge-no-f-f.png)

6. Ver el historial
![](img/E2-git-log-graph.png)



### **3. Fusión squash (git merge --squash)**

1.  Crer un nuevo repositorio
![](img/E3-crear-repositorio.png)

2. Agregar un archivo inicial en la rama principal (main)
![](img/E3-primer-commit.png)

3. Crear y cambiar a una nueva rama `add-basic-files`
![](img/E3-branch-squash.png)

4. Hacer algunos cambios y comitearlos
![](img/E3-segundo-commit.png)

    y otro cambio
![](img/E3-tercer-commit.png)

5. Cambiar de vuelta a la rama `main` y realizar la fusión squash
![](img/E3-merge-squash.png)

6. Para completar la fusión squash, realiza un commit:
![](img/E3-squash-final.png)


## **Ejercicios**

### **Resolver conflictos en una fusión non-fast-forward**

1. Inicializa un nuevo repositorio
![](img/C1-iniciar-repositorio.png)

2. Crea un archivo index.html y realiza un commit en la rama main:
![](img/C1-primer-commit.png)

3. Crea y cambia a una nueva rama feature-update y realiza un commit en la rama feature-update
![](img/C1-commit-branch-feature.png)


4. Regresa a la rama main y realiza una edición en el mismo archivo
![](img/C1-commit-branch-main.png)

6. Fusiona la rama feature-update con --no-ff y observa el conflicto
![](img/C1-conflicto-vsc.png)

7. Solucion al conflicto y Vemos el  historial
![](img/C1-conflicto-resuelto.png)

**Preguntas:**
- ¿Qué pasos adicionales tuviste que tomar para resolver el conflicto?
    - Tuve que editar el archivo `index.html` manualmente, y elimine los bloques `<<<<<<< HEAD`, `==============`, `>>>>>>>>>>>>>>>>>>> feature-update`
- ¿Qué estrategias podrías emplear para evitar conflictos en futuros desarrollos colaborativos?
    - Revisar y entender el historial de cambios antes de hacer una fusion de reamas `merge`, con comandos como git log, git diff, o git status
    - Realizar revisiones de codigo antes de fusionar ramas
    - Usar ramas pequenas y de corta duracion , para que los merges sean mas simples y sean menos propensoss a tener conflictos

### **Comparar los historiales con git log después de diferentes fusiones**

- Creamos el repositorio
![](img/C2-1-CREAMOS-REPOSITORIO.png)

- Modificamos el archivo en las ramas `main` y `feature-1`
![](img/C2-2-commit-main-feature-1.png)

- Hacemos commit en la rama `feature-2`
![](img/C2-3-COMMIT-FEATURE-2.png)

- Hacemos `merge` con la rama `feature-1`
![](img/C2-4-MERGE-FEATURE-1.png)

- Hacemos `merge` con la rama `feature-2` y solucionamos el conflicto 
![](img/C2-5-MERGE-FEATURE-2-SOL.png)

- Hacemos commit en la ram a `feature--3`
![](img/C2-6-COMMIT-FEATURE-3.png)

- Hacemos `merge squash` con la rama `feature--3`
![](img/C2-7-MERGE-SQUASH.png)

- Generamos los graficos logs
![](img/C2-8-GRAPH-LOG.png)

Vemos que se hizo correctamente el `merge squash`

- **Preguntas:**
    - ¿Cómo se ve el historial en cada tipo de fusión?
        - Para el **fast-forward:** el historial se linela como si los commits se hubieran hecho en el `main`
        - Para el **Non-fast-forward** se ve una ramificacion  y un punto de union
        - Para el **squash** apesar de hubo varios commits, estos se comprimieron 

    - ¿Qué método prefieres en diferentes escenarios y por qué?
        - el **fast-forward:** cuando hay cambios simples como errores o documenteacion
        - el **Non-fast-forward** cuando la rama tiene multiples cambioss y necesito ver que fue parte de una sola funcionalidad especifica
        -  el **squash** para manterner historial limpio y no necestito detalle de cada commit
