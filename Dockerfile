FROM python:3.12-slim

WORKDIR /app/backend

# Copy only requirements first for caching benefits
COPY requirements.txt .

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc default-libmysqlclient-dev pkg-config && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files after installing dependencies
COPY . .

# Expose the port
EXPOSE 8000

# Use a script to handle migrations and Gunicorn startup
CMD ["sh", "-c", "python manage.py migrate --no-input && gunicorn todoList.wsgi:application --bind 0.0.0.0:8000"]
