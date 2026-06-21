## Parent image
FROM python:3.10-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## Work directory inside the docker container
WORKDIR /app

## Installing system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Copying all contents from local to app
COPY . .

## Run setup.py (installs requirements.txt too, via install_requires)
RUN pip install --no-cache-dir -e .

## Used PORTS
EXPOSE 8501

## Healthcheck (optional but good practice for Streamlit)
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

## Run the app
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]