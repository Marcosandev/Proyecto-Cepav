import flet as ft
import flet_audio as fta
# Asegúrate de importar tu función de consultas

class PlaylistView(ft.Column): # O ft.Container, según uses
    def __init__(self, page: ft.Page):
        super().__init__()
        # CAMBIO CLAVE: Usa self.main_page en lugar de self.page
        self.main_page = page 
        self.expand = True