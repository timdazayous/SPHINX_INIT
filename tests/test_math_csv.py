import pandas as pd
import pytest

# On importe les fonctions de notre module
from app.modules.mon_module import add, print_data, square, sub


# --- 1. TESTS PARAMÉTRÉS ---
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 12),
        (20, 2, 22),
        (0, 2, 2),
        (-5, 5, 0),
    ],
)
def test_add(a, b, expected):
    """Teste l'addition avec plusieurs jeux de données."""
    assert add(a, b) == expected


def test_sub():
    """Teste la soustraction."""
    assert sub(10, 5) == 5
    assert sub(0, 5) == -5


def test_square():
    """Teste la mise au carré."""
    assert square(4) == 16
    assert square(0) == 0


# --- 2. FIXTURES ---
@pytest.fixture
def dummy_dataframe():
    """Génère un DataFrame temporaire en mémoire pour les tests."""
    data = {
        "id": [1, 2, 3],
        "nom": ["Test1", "Test2", "Test3"],
        "age": [20, 30, 40],
    }
    return pd.DataFrame(data)


def test_print_data(dummy_dataframe):
    """Teste le comptage de lignes avec le faux DataFrame."""
    resultat = print_data(dummy_dataframe)
    assert resultat == 3
