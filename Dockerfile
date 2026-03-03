# 1. Utiliser une image de base légère
FROM python:3.11-slim

# 2. Définir le dossier de travail
WORKDIR /workspace

# 3. Installer uv
RUN pip install uv

# 4. Copier les dépendances
COPY pyproject.toml uv.lock ./

# 5. Installer les dépendances
RUN uv sync --no-dev --system

# 6. Copier le code
COPY app/ ./app/

# 7. Lancer l'application
CMD ["python", "app/main.py"]
