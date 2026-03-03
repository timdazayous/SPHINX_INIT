import pandas as pd
from modules.mon_module import add, print_data, square, sub


def main():
    """Point d'entrée principal de l'application."""
    print("--- Tests Mathématiques ---")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {sub(10, 5)}")
    print(f"Carré de 4 = {square(4)}")

    print("\n--- Analyse de données ---")
    try:
        # Lecture du fichier CSV local
        df = pd.read_csv("app/moncsv.csv")
        nb_lignes = print_data(df)
        print(f"\nLe fichier contient {nb_lignes} lignes.")
    except FileNotFoundError:
        print("Erreur : Le fichier 'app/moncsv.csv' est introuvable.")


if __name__ == "__main__":
    main()
