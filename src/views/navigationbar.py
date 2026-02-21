import flet as ft

class NavigationBar(ft.NavigationBar):
    def __init__(self, page: ft.Page):
        super().__init__()
        # Cambiamos 'self.page' por 'self.main_page' para evitar conflicto
        self.main_page = page 
        
        self.destinations = [
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.LIBRARY_MUSIC, label="Playlist"),
        ]
        self.on_change = self.cambiar_vista

    def cambiar_vista(self, e):
        # Usamos la nueva referencia
        index = e.control.selected_index
        if index == 0:
            self.main_page.go("/")
        elif index == 1:
            self.main_page.go("/playlist")