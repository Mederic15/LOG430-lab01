"""
User view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from models.user import User
from controllers.user_controller import UserController
from views.menu_view import MenuView


class UserView:
    @staticmethod
    def show_options():
        controller = UserController()

        menu_options = [
            "Montrer la liste d'utilisateurs",
            "Ajouter un utilisateur",
            "Quitter l'appli"
        ]

        while True:
            MenuView.show_menu(menu_options)
            choice = MenuView.get_choice()

            if choice == '1':
                users = controller.list_users()
                UserView.show_users(users)

            elif choice == '2':
                name, email = UserView.get_inputs()
                user = User(None, name, email)
                controller.create_user(user)

            elif choice == '3':
                controller.shutdown()
                break

            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_users(users):
        print("\n".join(
            f"{user.id}: {user.name} ({user.email})"
            for user in users
        ))

    @staticmethod
    def get_inputs():
        name = input("Nom d'utilisateur : ").strip()
        email = input("Adresse courriel : ").strip()
        return name, email