# Usa una imagen de Python como base
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de aplicación al contenedor
COPY app.py .
COPY requirements.txt

# Instala Flask
RUN pip install -r requirements.txt

# Expone el puerto 5000
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
