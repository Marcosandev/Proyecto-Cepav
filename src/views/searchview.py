import flet as ft

class SearchView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.controls = [
            ft.Text("Buscar", size=24, weight="bold"),
            ft.Text("Aquí puedes buscar tus canciones favoritas", size=16, weight="bold"),
        ]