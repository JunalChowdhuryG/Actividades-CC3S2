
# Trivia Game  
**Autor:** Junal Johir Chowdhury Gomez – `20200092K`  

Este proyecto es un juego de trivia desarrollado en **Python** y completamente **dockerizado**, lo que permite ejecutarlo fácilmente sin necesidad de instalar dependencias ni configurar entornos locales.

## ¿Cómo ejecutarlo?

Solo necesitas seguir estos pasos:

1. **Clona el repositorio:**

```bash
git clone https://github.com/JunalChowdhuryG/Prueba_entrada_CC3S2.git
```

2. **Accede a la carpeta del proyecto:**

```bash
cd Prueba_entrada_CC3S2
```

3. **Levanta la aplicación con Docker Compose:**

```bash
docker-compose up -d --build
```

4. **Abre tu navegador y visita:**

```
http://localhost:5000
```

¡Y listo! Ya puedes comenzar a disfrutar del juego de trivia desde tu navegador.

##  Sobre el juego

- El juego presenta preguntas aleatorias desde una base de datos PostgreSQL.
- Puedes elegir el nivel de dificultad.
- Al final, recibirás un resumen con tu puntuación.