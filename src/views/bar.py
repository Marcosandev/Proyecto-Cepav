import flet as ft

class Bar(ft.Column): 
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.PERSON), # 0
                ft.NavigationBarDestination(icon=ft.Icons.HOME),   # 1
                ft.NavigationBarDestination(icon=ft.Icons.SEARCH), # 2
                ft.NavigationBarDestination(icon=ft.Icons.MOVIE),  # 3
                ft.NavigationBarDestination(icon=ft.Icons.MAIL),   # 4
            ],
            on_change=self.cambiar_vista
        )

    def cambiar_vista(self, e):
        opcion = e.control.selected_index
        
        # --- IMPORTACIONES LOCALES ---
        # Movemos esto aquí para romper el ciclo de error
        from src.views.homeview import HomeView
        from src.views.searchview import SearchView
        from src.views.playlistview import PlaylistView
        from src.views.moreview import MoreView

        self.page.controls.clear()
        
        if opcion == 0:
            self.page.add(HomeView(self.page))
        elif opcion == 1:
            self.page.add(SearchView(self.page))
        elif opcion == 2:
            self.page.add(PlaylistView(self.page))
        elif opcion == 3:
            self.page.add(MoreView(self.page))
        
        self.page.update()