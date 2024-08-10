# Usamos una imagen base de Python
FROM python:3.10-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo de requisitos y los instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente de la aplicación
COPY . .

# Copiamos el archivo .env al contenedor (opcional)
COPY .env .

# Exponemos el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
