# **Actividad 4: Introduccion a Git - conceptos basicos y operaciones esenciales**


## **Preguntas:**
### **1. ¿De que manera Git te ha ayudado a mantener un historial estructurado y ordenado de tus cambios?**  

A lo largo de mis proyectos , tanto en este curso como en otros, Git ha sido una herramienta clave para organizar y gestionar el historial de cambios de manera eficiente. Algunas de las formas en que me ha beneficiado incluyen:  

- **Commits Descriptivos**: Cada modificacion en mi codigo va acompañada de un commit con un mensaje claro y detallado. Esto me permite entender posteriormente que cambios se realizaron y porque , facilitando la comprension del contexto en proyectos complejos  

- **Uso de Ramas (Branches)**: Trabajo con ramas para desarrollar nuevas funcionalidades o probar ideas sin afectar la rama principal (main). Esto me ayuda a mantener el codigo estable mientras experimento con mejoras o soluciones

- **Reversion de Cambios**: en ocasiones , he implementado cambios que generaron problemas. Gracias a Git, he podido revertirlos facilmente y restaurar una version anterior del codigo sin comprometer la estabilidad del proyecto  

- **Comparacion de Versiones (Diffs)**: Git me permite analizar las diferencias entre versiones del codigo, lo que resulta util para identificar la causa de errores o entender la evolucion de los cambios 

- **Colaboracion Eficiente**: cuando trabajo en equipo, Git facilita la coordinacion de cambios. Cada miembro puede hacer commits y fusionar su trabajo en una rama comun, permitiendo un seguimiento claro de las contribuciones y optimizando la revision del codigo.  

- **Etiquetado de Versiones Clave**: En algunos proyectos, utilizo etiquetas (tags) para marcar versiones importantes, como lanzamientos o hitos significativos. Esto simplifica la navegacion por el historial del proyecto y la gestion de versiones  

- **Respaldo y Acceso Remoto**: con plataformas como GitHub, puedo mantener copias remotas de mis proyectos. Esto no solo actua como respaldo en caso de fallos en mi equipo, sino que tambien me permite acceder a mi codigo desde cualquier lugar y colaborar con otros desarrolladores de manera sencilla


### **2. ¿Que ventajas encuentras en el uso de ramas para desarrollar nuevas funciones o corregir errores?**  

El uso de ramas en Git aporta multiples beneficios cuando se trabaja en el desarrollo de nuevas caracteristicas o en la correccion de errores. Algunas de sus ventajas clave incluyen :  

- **Aislamiento de Cambios**: Cada rama permite trabajar de manera independiente en una nueva funcionalidad o correccion sin afectar la rama principal (`main`). Esto garantiza que el codigo en produccion se mantenga estable mientras se implementan y prueban los cambios  

- **Trabajo en Paralelo**: Varios desarrolladores pueden trabajar simultaneamente en diferentes ramas sin interferir entre si. Esto facilita la colaboracion y permite avanzar en diversas tareas al mismo tiempo , optimizando la eficiencia del equipo  

- **Mayor Control de Calidad**: Al desarrollar en una rama separada, es posible realizar pruebas exhaustivas y revisiones de codigo antes de fusionar los cambios con la rama principal. Esto ayuda a prevenir la insercion de errores en el codigo estable  

- **Flexibilidad para Descartar Cambios**: Si una nueva funcionalidad o correccion no funciona como se esperaba, se puede eliminar la rama sin afectar el codigo base. Esto proporciona una gran seguridad y flexibilidad en el desarrollo  

- **Despliegues Independientes**: En proyectos con lanzamientos frecuentes, las ramas permiten preparar y probar versiones especificas de forma independiente. Una vez que una funcion esta lista, puede fusionarse y desplegarse sin depender de otros cambios en desarrollo

### **Realiza una revisión final del historial de commits para asegurarte de que todos los cambios se han registrado correctamente.**
### **Revisa el uso de ramas y merges para ver cómo Git maneja múltiples líneas de desarrollo.**
- Ya habiendo terminado la Actividad 4, procederemos a revisar el historial de commits
- Aplicando el comando `git log --oneline --graph --all`
![](img/log-final.png)
- A lo largo de la actividad podemos apreciar el uso de ramas, el cual permite flexibilidad en el desarrollo, ya sea para hacer despliegues independientes, lo cual permite preparar y probar versiones especificas de forma independiente, una vez que una funcion esta lista, puede fusionarse sin afectar a las demas.




## **Ejercicios**

### **Ejercicio 1: Manejo avanzado de ramas y resolución de conflictos**

Primero configo git con mis credenciales
    ![Configuracion](img/E1-git-config.png)

Para mi caso, yo manejo 2 cuentas github en mi laptop a travez de claves ssh, para este repositorio estare manejando la cuenta:

```bash
file:C:/Users/Junal/.gitconfig  user.email=chowdhurygomezjunaljohir@gmail.com
file:C:/Users/Junal/.gitconfig  user.name=JunalChowdhuryG
```

1. **Crear una nueva rama para una característica:**

    - Crea una nueva rama llamada feature/advanced-feature desde la rama main:

    ```git
    git branch feature/advanced-feature
    git checkout feature/advanced-feature       
    ```
    ![](img/E1-git-branch-feature-advanced.png)


2. **Modificar archivos en la nueva rama:**

    - Edita el archivo main.py para incluir una función adicional:

        El código agregado nos permite imprimer el mensaje `Hello from advanced feature` mediante la funcion **greet**
        ![](img/E1-touch-nano-mainPY.png)

    - Añadimos y confirmamos estos cambios en la rama feature/advanced-feature:

        ```git
        git add main.py
        git commit -m "Add greet function in advanced feature"     
        ```
        ![](img/E1-git-commit-advanced-mainPY.png)

3. **Simular un desarrollo paralelo en la rama main:**

    - Cambia de nuevo a la rama main:

        ```git
        git checkout main  
        ```
    - Añade y confirma estos cambios en la rama main:

        ```git
        git add main.py
        git commit -m "Update main.py message in main branch"
        ```
    ![](img/E1-git-commit-main-mainPY.png)

4. **Intentamos fusionar la rama feature/advanced-feature en main:**

    - Fusiona la rama feature/advanced-feature en main:
        ```git
        git merge feature/advanced-feature
        ```
    Observamos que surgio un conflicto al momento de hacer un merge.

    ![](img/E1-git-conflict-1.png)

    Observamos que los prints creadas en el archivo python en las diferentes ramas se unen. 

    ![](img/E1-codigo-conflicto.png)

5. **Resolver el conflicto de fusión:**

    - Git generará un conflicto en main.py. Abre el archivo y resuelve el conflicto manualmente,
    eligiendo cómo combinar las dos versiones.

    - Después de resolver el conflicto, añade el archivo resuelto y completa la fusión:

        ```git
        git add main.py
        git commit -m "Resolve merge conflict between main and feature/advanced-feature"
        ```
    ![](img/E1-git-merge-1.png)

6. **Eliminar la rama fusionada:**
    - Una vez que hayas fusionado con éxito y resuelto los conflictos, elimina la rama
    feature/advanced-feature:

        ```git
        git branch -d feature/advanced-feature
        ```

    ![](img/E1-git-delete-branch.png)

### **Ejercicio 2: Exploración y manipulación del historial de commits**

1. **Ver el historial detallado de commits:**
   - Usa el comando `git log` para explorar el historial de commits, pero esta vez con más detalle:

     ```bash
     $ git log -p
     ```
    ![](img/E2-git-log-p.png)
    - Podemos parte del historial de commits


2. **Filtrar commits por autor:**
   - Usa el siguiente comando para mostrar solo los commits realizados por un autor específico:

     ```bash
     $ git log --author="TuNombre"
     ```
     ![](img/E2-git-log-author.png)
    - Podemoss ver els historial del author=`JunalChowdhuryG`

3. **Revertir un commit:**
   - Imagina que el commit más reciente en `main.py` no debería haberse hecho. Usa `git revert` para revertir ese commit:

     ```bash
     $ git revert HEAD
     ```
   ![](img/E2-git-revert-head.png)
   - Revertimos la ultima modificacion del `main.py`

4. **Rebase interactivo:**
   - Realiza un rebase interactivo para combinar varios commits en uno solo. Esto es útil para limpiar el historial de commits antes de una fusión.
   - Usa el siguiente comando para empezar el rebase interactivo:

     ```bash
     $ git rebase -i HEAD~3
     ```
    - El comaando anterior abre en el editor:
    ![](img/E2-git-revert-3-editor.png)

    - Cambiamos los terminos  `pick` a `squach`
    ![](img/E2-git-revert-3-squash.png)

    - Vemos los cambios hechoss
    ![](img/E2-git-revert-3-terminal.png)


5. **Visualización gráfica del historial:**
   - Usa el siguiente comando para ver una representación gráfica del historial de commits:

     ```bash
     $ git log --graph --oneline --all
     ```
    - visualizamos el git logs
   ![](img/E2-git-log%20-graph.png)
   - otra manera de visualizar es con el comando `gitk --all`
   ![](img/E2-gitk-all.png)

### **Ejercicio 3: Creación y gestión de ramas desde commits específicos**

1. **Crear una nueva rama desde un commit específico:**
   - Usa el historial de commits (`git log --oneline`) para identificar un commit antiguo desde el cual crear una nueva rama:
     ```bash
     $ git log --oneline
     ```
    ![](img/E3-git-log-oneline.png)
    - Tomaremos el commit con hash: `03c7016`

   - Crea una nueva rama `bugfix/rollback-feature` desde ese commit:

     ```bash
     $ git branch bugfix/rollback-feature 03c7016
     $ git checkout bugfix/rollback-feature
     ```
    ![](img/E3-git-branch-bugfix-rollback.png)


2. **Modificar y confirmar cambios en la nueva rama:**
   - Realiza algunas modificaciones en `main.py` que simulen una corrección de errores:
     ```python
     def greet():
         print('Fixed bug in feature')
     ```
   - Añade y confirma los cambios en la nueva rama:

     ```bash
     $ git add main.py
     $ git commit -m "Fix bug in rollback feature"
     ```
     
3. **Fusionar los cambios en la rama principal:**
   - Cambia de nuevo a la rama `main` y fusiona la rama `bugfix/rollback-feature`:

     ```bash
     $ git checkout main
     $ git merge bugfix/rollback-feature
     ```
    ![](img/E3-git-merge.png)


4. **Explorar el historial después de la fusión:**
   - Usa `git log` y `git log --graph` para ver cómo se ha integrado el commit en el historial:

     ```bash
     $ git log --graph --oneline
     ```
     ![](img/E3-git-log-oneline.png)


5. **Eliminar la rama bugfix/rollback-feature:**
   - Una vez fusionados los cambios, elimina la rama `bugfix/rollback-feature`:

     ```bash
     $ git branch -d bugfix/rollback-feature
     ```
    ![](img/E3-delete-branch.png)

### **Ejercicio 4: Manipulación y restauración de commits con git reset y git restore**
1. **Hacer cambios en el archivo main.py:**
   - Edita el archivo `main.py` para introducir un nuevo cambio:
     ```python
     print('This change will be reset')
     ```
     ![](img/E4-git-echo-main.png)
   - Añade y confirma los cambios:

     ```bash
     $ git add main.py
     $ git commit -m "Introduce a change to be reset"
     ```
     ![](img/E4-git-commit-change-reset.png)



2. **Usar git reset para deshacer el commit:**
   - Deshaz el commit utilizando `git reset` para volver al estado anterior:

     ```bash
     $ git reset --hard HEAD~1
     ```
   - Verifica que el commit ha sido eliminado del historial y que el archivo ha vuelto a su estado anterior.
   ![](img/E4-git-reset-head.png)

   - Podemos observar que se ha eliminado el commit, comparando el `git status` antes y despues del `git reset --hard HEAD~1`

3. **Usar git restore para deshacer cambios no confirmados:**
   - Realiza un cambio en `README.md` y no lo confirmes:
   - En mi caso hare la modificacion en el `ANNOTATION.md`

     ```bash
     $ echo "Another line in ANNOTATION" >> ANNOTATION.md
     $ git status
     ```
    ![](img/E4-echo-annotation.png)

   - Usa `git restore` para deshacer este cambio no confirmado:

     ```bash
     $ git restore README.md
     ```
   - Verifica que el cambio no confirmado ha sido revertido.
    ![](img/E4-git-restore.png)

    - Podemos observar que despues de `git restore` el archivo `ANNOTATION.md` no contiene el mensaje "Another line in ANNOTATION", y el archivo `main.py` no contiene la ultima modificacion 
    ```python
     print('This change will be reset')
     ```

### **Ejercicio 5: Trabajo colaborativo y manejo de Pull Requests**
- Como mencione anteriormente, manejo 2 cuentas de github las cuales utilizare para hacer el Pull Request desde una cuenta a otra:

  - [JunalChowdhuryG (Principal): Actividades-CC3S2](https://github.com/JunalChowdhuryG/Actividades-CC3S2)  
  - [JunalChowdhuryGomez (Secundaria): Fork-Segunda-Cuenta-Actividades-CC3S2](https://github.com/JunalChowdhuryGomez/Fork-Segunda-Cuenta-Actividades-CC3S2)

- Repositorio de la cuenta **Principal** vista desde la cuenta **Secundaria**.
![](img/E5-repositorio-visto-otra-cuenta.png)

- Haciendo Fork del repositoria de la cuenta **Principal** en la cuenta **Secundaria**, el repositorio es: [JunalChowdhuryGomez/Fork-Segunda-Cuenta-Actividades-CC3S2](https://github.com/JunalChowdhuryGomez/Fork-Segunda-Cuenta-Actividades-CC3S2)
![](img/E5-Fork-segunda-cuenta.png)

- Creo el archivo `collaboration.py` en la rama `feature/team-feature`  en el repositorio de la cuenta **Secundaria**
![](img/E5-creacion-archivo-rama-feature-team-feature.png)

- Procedemos hacer el commit desde la segunda cuenta
![](img/E5-commit-segunda-cuenta.png)

- Preparamos el pull request desde la segunda cuenta

![](img/E5-preparando-pull-request-segunda-cuenta.png)

- Añadimos el mensaje al pull request 
![](img/E5-pull-request-segunda-cuenta.png)

- Confirmamos el envio del pull request desde la segunda cuenta
![](img/E5-confirmacion-pull-request-segunda-cuenta.png)

- En la cuenta **principal** verificamos el pull request
![](img/E5-pull-request-cuenta-principal.png)

- Revisamos el pull request 
![](img/E5-revision-pull-request.png)

- Aceptamos el pull request desde la cuenta **Principal**
![](img/E5-aceptando-pull-request-segunda-cuenta.png)

- Fusionamos a la rama main
![](img/E5-merge-a-main-cuenta-principal.png)

- Verificamos que se fuciono la rama correctament, ademas podemo ver la contribucion de la segunda cuenta de github
![](img/E5-verificacion-colaboracion.png)

### **Ejercicio 6: Cherry-Picking y Git Stash**

- Hacer cambios en main.py y confirmarlos:
![](img/E6-git-commit-main.png)

- Crear una nueva rama
![](img/E6-git-branch.png)

- Vemos el hash el historial
![](img/E6-git-log-oneline.png)

- Aplicamos `cherry-pick` con el hash `3727ae7`
![](img/E6-git-cherry-pick.png)

- Modificacmos el `main.py` y hacemos `git stash`
![](img/E6-modificacion-main.png)

- Recuperamos los cambios guardados
![](img/E6-git-stach-pop.png)

- Verificamos con el `git log`
![](img/E6-git-log.png)