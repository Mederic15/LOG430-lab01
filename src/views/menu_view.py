class MenuView:
    @staticmethod
    def show_menu(options: list[str]):
        print()
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

    @staticmethod
    def get_choice():
        return input("Choisissez une option: ")