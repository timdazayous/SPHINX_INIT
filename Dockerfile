# 1. Utiliser une image de base légère (Consigne du TP)
FROM python:3.11-slim

# 2. Définir le dossier de travail dans le conteneur
WORKDIR /workspace

# 3. Installer uv dans le conteneur
RUN pip install uv

# 4. Copier uniquement les fichiers de dépendances (pour optimiser le cache Docker)
COPY pyproject.toml uv.lock ./

# 5. Installer les dépendances avec uv 
# (--system installe directement dans le Python du conteneur, pas besoin de .venv)
RUN uv sync --no-dev --system

# 6. Copier le reste du code source
COPY app/ ./app/

# 7. Commande pour lancer l'application (Consigne du TP)
CMD ["python", "app/main.py"]
