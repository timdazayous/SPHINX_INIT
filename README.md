<<<<<<< Updated upstream
=======
# 🧰 Toolbox MLOps - Fondation et Excellence Technique

![CI Status](https://github.com/timdazayous/SPHINX_INIT/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![uv](https://img.shields.io/badge/uv-fast-magenta.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Ce projet constitue une boîte à outils ("Toolbox") de référence pour le développement de projets en Intelligence Artificielle et MLOps. Il fournit un environnement de développement professionnel, standardisé, testé, documenté et prêt à être conteneurisé.

## 🚀 Fonctionnalités principales

* **Gestion ultra-rapide des dépendances** via `uv`.
* **Qualité de code stricte** assurée par `Ruff` (linter et formateur).
* **Tests unitaires robustes** avec `Pytest` (fixtures, paramétrisation, 100% coverage).
* **Documentation dynamique** générée par `Sphinx` (thème Furo).
* **Conteneurisation native** prête pour la production avec `Docker`.
* **Intégration Continue (CI)** automatisée avec `GitHub Actions`.

---

## 🛠️ Guide d'installation

Ce projet utilise [uv](https://github.com/astral-sh/uv), un gestionnaire de paquets Python écrit en Rust, incroyablement rapide.

### 1. Prérequis
* Python 3.11 ou supérieur
* Installer `uv` sur votre machine : `pip install uv`

### 2. Cloner et initialiser le projet
Clonez le dépôt, puis utilisez la commande `uv sync` pour recréer l'environnement virtuel exact (défini par le fichier `uv.lock`) avec toutes les dépendances de développement.

    git clone https://github.com/timdazayous/SPHINX_INIT.git
    cd SPHINX_INIT
    uv sync --all-extras --dev

### 3. Commandes utiles
* **Lancer l'application** : `uv run python app/main.py`
* **Vérifier le code** : `uv run ruff check .`
* **Lancer les tests** : `uv run pytest`
* **Générer la doc** : `cd docs && uv run ./make.bat html`

---

## 🐳 Déploiement Docker

Une image de base légère est fournie pour garantir un environnement reproductible :

    # Construire l'image
    docker build -t toolbox-mlops .

    # Lancer le conteneur
    docker run toolbox-mlops

---

## 🤝 Contribuer au projet

Les contributions sont les bienvenues ! Pour proposer une modification :
1. Créez une branche (`feat/ma-nouvelle-fonctionnalite`).
2. Assurez-vous que le code passe le linter (`uv run ruff check .`).
3. Assurez-vous de maintenir 100% de couverture de test (`uv run pytest`).
4. Ouvrez une **Pull Request**.

Veuillez consulter notre fichier [CONTRIBUTING.md](.github/CONTRIBUTING.md) pour plus de détails sur le processus de développement.

---

## 📜 Code de conduite

Afin de garantir un environnement sain et constructif, nous demandons à tous les contributeurs de respecter notre [CODE_OF_CONDUCT.md](.github/CODE_OF_CONDUCT.md).

---

## 👥 Contributeurs

* **Tim** (@timdazayous) - *Développement initial & MLOps setup*

---

## 📄 Licence

Ce projet est sous licence **MIT**. Vous êtes libre de l'utiliser, de le modifier et de le distribuer. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.
>>>>>>> Stashed changes
