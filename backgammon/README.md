# Backgammon - CLI y Pygame

## Requisitos
- Python 3.11
- Docker y Docker Compose (para ejecutar como pide la cátedra)

## Instalación local
pip install -r requirements.txt

## Ejecutar CLI
python cli/main.py

## Ejecutar UI Pygame
python pygame_ui/main.py

## Testing
pytest --cov=core --maxfail=1 -q

## Docker - modo juego (CLI)
docker compose -f docker/docker-compose.yml up --build app

## Docker - modo testing
docker compose -f docker/docker-compose.yml up --build tests
