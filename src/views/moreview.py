import flet as ft

class MoreView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.controls = [
            ft.Text("Más", size=24, weight="bold"),
            ft.Text("Aquí puedes encontrar más opciones y configuraciones", size=16, weight="bold"),
        ]