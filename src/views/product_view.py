from models.product import Product
from controllers.product_controller import ProductController
from views.menu_view import MenuView


class ProductView:
    @staticmethod
    def show_options():
        controller = ProductController()

        menu_options = [
            "Montrer la liste de produits",
            "Ajouter un produit",
            "Supprimer un produit",
            "Quitter l'appli"
        ]

        while True:
            MenuView.show_menu(menu_options)
            choice = MenuView.get_choice()

            if choice == '1':
                products = controller.list_products()
                ProductView.show_products(products)

            elif choice == '2':
                name, brand, price = ProductView.get_inputs()
                product = Product(None, name, brand, price)
                controller.create_product(product)

            elif choice == '3':
                product_id = input("Entrez l'ID du produit à supprimer: ")
                controller.delete_product(product_id)

            elif choice == '4':
                controller.shutdown()
                break

            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_products(products):
        print("\n".join(
            f"{product[0]}: {product[1]} ({product[2]}, ${product[3]})"
            for product in products
        ))

    @staticmethod
    def get_inputs():
        name = input("Nom du produit : ").strip()
        brand = input("Marque du produit : ").strip()
        price = float(input("Prix du produit : ").strip())
        return name, brand, price