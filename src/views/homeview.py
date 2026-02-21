import flet as ft

class HomeView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.controls = [
            ft.Text("Bienvenido a Music App", size=24, weight="bold"),
            ft.Text("Selecciona una opción en la barra inferior"),
        ]