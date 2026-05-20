"""
Store manager application
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

#HA
from views.menu_view import MenuView
from views.product_view import ProductView
from views.user_view import UserView

if __name__ == "__main__":
    print("===== LE MAGASIN DU COIN =====")

    menu_options = [
        "Produits",
        "Utilisateurs",
        "Quitter"
    ]

    while True:
        MenuView.show_menu(menu_options)
        choice = MenuView.get_choice()

        if choice == "1":
            ProductView.show_options()

        elif choice == "2":
            UserView.show_options()

        elif choice == "3":
            print("Au revoir!")
            break

        else:
            print("Option invalide")