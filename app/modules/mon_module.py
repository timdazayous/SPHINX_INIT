import pandas as pd


def add(a: float, b: float) -> float:
    """Additionne deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.

    Returns:
        float: La somme de a et b.

    """
    return a + b


def sub(a: float, b: float) -> float:
    """Soustrait deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.

    Returns:
        float: La différence entre a et b.

    """
    return a - b


def square(a: float) -> float:
    """Calcule le carré d'un nombre.

    Args:
        a (float): Le nombre à élever au carré.

    Returns:
        float: Le carré du nombre a.

    """
    return a**2


def print_data(df: pd.DataFrame) -> int:
    """Affiche un DataFrame et retourne son nombre de lignes.

    Args:
        df (pd.DataFrame): Le DataFrame Pandas à analyser.

    Returns:
        int: Le nombre de lignes présentes dans le DataFrame.

    """
    print(df)
    return len(df)
