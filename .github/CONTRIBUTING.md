# Guide de Contribution

Merci de l'intérêt que vous portez à ce projet ! Voici les règles à suivre pour garantir la qualité de la "Toolbox MLOps".

## Le Workflow de Développement

1. Ne travaillez **jamais** directement sur la branche `main`.
2. Créez toujours une branche pour votre fonctionnalité : `git checkout -b feat/nom-fonctionnalite`.
3. Assurez-vous que votre environnement virtuel est à jour : `uv sync`.

## Les standards de Qualité (Obligatoires)

Avant de soumettre une Pull Request, votre code doit valider ces deux étapes locales :

### 1. Linting et Formatage
Nous utilisons **Ruff**. Votre code doit être propre :

    uv run ruff check .

*(Si des erreurs apparaissent, vous pouvez utiliser `uv run ruff check --fix .`)*.

### 2. Tests et Couverture
Nous utilisons **Pytest**. Le code doit conserver **100% de couverture** :

    uv run pytest

## Soumettre votre travail
1. Poussez votre branche sur GitHub.
2. Ouvrez une Pull Request vers `main`.
3. Le robot `GitHub Actions` vérifiera automatiquement votre code.
4. Si le robot affiche une croix rouge, corrigez les erreurs sur votre branche avant de demander une revue de code.
