import flet as ft
from .navigationbar import NavigationBar

class HomeView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.controls = [
            ft.Text("Inicio", size=24, weight="bold"),
            ft.Text("La mejor playlist del momento", size=16, weight="bold"),
        ]