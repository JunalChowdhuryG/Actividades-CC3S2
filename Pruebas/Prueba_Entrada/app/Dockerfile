FROM python:3.11-slim

WORKDIR /app

# copiamos el archivo de requerimientos
COPY app/requirements.txt .

# instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# copiamos el resto de archivos de la app
COPY app/ .

# para ejecutar la interfaz en navegador (localhost:5000)
CMD ["python", "app.py"]

# para ejecutar la interfaz enterminal
#CMD ["python", "main.py"]
