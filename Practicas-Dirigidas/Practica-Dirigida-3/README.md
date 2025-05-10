# **Practica Dirigida 3**

Este repo contiene la coleccion de scripts Bash que se implemento en ejemplos y ejercicios de la Practica Dirigida3

## Estructura
* `ejemplos/`: Scripts conceptos basicos de Bash
    - `ls_custom.sh`: imprimte archivos ordenadoss y con colores
    - `hello.sh`: imprime "hello  World" 
    - `variables.sh`: uso de variables 
    - `params.sh`: manejo de parametros
    - `arrays.sh`: arrays y arrays asociativos
    - `arithmetic.sh`: operaciones aritmeticas
    - `substitution.sh`: substitucion de comandos para fechas y conteos
    - `expansions.sh`: muestra expansiones de variables
    - `pipes.sh`:  pipes y redirecciones de salida/errores
    - `conditionals.sh`:  condicionales `if` para verificar numeros pares/impares
    - `case.sh`: estructura `case` para  tipos de archivos por extension
    - `loops.sh`:  bucles `for`, `while` y `until`
    - `functions.sh`: funciones para saludos y divisiones
    - `debug.sh`: opciones de depuracion (`set -xe`, `trap`)
    - `regex.sh`: valida emails con expresione regulares

* `ejercicios/`: Soluciones a los ejercicios propuestos como:
    - `marco.sh`:  funciones `marco` y `polo` para guardar y restaurar
    - `capture_failure.sh`: ejecuta un comando hasta que falle capturando salida y errores
    - `zip_html.sh`: comprime archivos html recursivamente en un archivo comprimidp
    - `latest_file.sh`: encuentra el archivo ms reciente y lista los archivos ordenados por fecha modificado

## Uso
1. Dar permiso a todos los scripts:
```bash
chmod +x ejemplos/*.sh ejercicios/*.sh
```

2. Ve al directorio que quieres:
   ```bash
   cd ejemplos
   ```
   o
   ```bash
   cd ejercicios
   ```

3. Ejecuta los scripts segun sea necesario:
   ```bash
   ./nombre_script.sh [parametros]
   ```
4. Algunos scripts requieren parametros especificos:
   - `ejemplos/conditionals.sh`: necesita un numero como argumento por ejemplo: `./conditionals.sh 4`
   - `ejemplos/case.sh`: necesita una extension de archivo por ejemplo: `./case.sh py`
   - `ejemplos/regex.sh`: necesita una direccion de correo  por ejemplo: `./regex.sh user@example.com`
   - `ejercicios/marco.sh`: necesita cargarse con `source marco.sh` para definir las funciones `marco` y `polo`

