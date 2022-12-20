from dataclasses import dataclass
from controllers.menu_manager import MenuManager


@dataclass
class ViewsMainMenu:

    def main():
        print("\n")
        print("-" * 30)
        print("Menu principal: ")
        print("-" * 30)
        MenuManager.main_menu()


