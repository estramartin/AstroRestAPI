# Utiliza la imagen base de Python para Django
FROM python:3.10.6

# Establece el directorio de trabajo en /app
WORKDIR /restonauta

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el contenido del proyecto al contenedor
COPY . .

# Expone el puerto 8000 para acceder al servidor Django
EXPOSE 8000

# Comando para iniciar el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]