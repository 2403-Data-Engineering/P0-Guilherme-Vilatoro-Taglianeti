from presentation.menu import MainMenu
from presentation.menu import Menu


class Terminal:
    def __init__(self):
        self.currentMenu = MainMenu()
        self.running = True

    def change_running_state(self):
        self.running = not self.running
    
    def change_Menu(self, menu:Menu):
        self.currentMenu = menu



    