import flet as ft
from src.views.bar import Bar

class SearchView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.page = page
        self.controls.append(ft.Text("Search", size=30))
        
        self.page.add(Bar(self.page)) 
        
        self.page.update()