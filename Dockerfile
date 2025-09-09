# Python Base Image
FROM python:3.11-slim

# System-Pakete für PostgreSQL installieren
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis
WORKDIR /app

# Requirements installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App-Code kopieren
COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/

# Non-root User (Sicherheit)
RUN useradd --create-home --shell /bin/bash appuser
RUN chown -R appuser:appuser /app
USER appuser

# Port freigeben
EXPOSE 5000

# App starten
CMD ["python", "app.py"]
