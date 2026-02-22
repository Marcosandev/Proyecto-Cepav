from email.mime import audio

import flet as ft
import flet_audio as fta
# Asegúrate de importar tu función de consultas

class PlaylistView(ft.Column): # O ft.Container, según uses
    def __init__(self, page: ft.Page):
        super().__init__()
        # CAMBIO CLAVE: Usa self.main_page en lugar de self.page
        self.main_page = page 
        self.expand = True
        
        # Lista visual donde irán las canciones
        self.lista_items = ft.ListView(expand=True, spacing=10)
        
        # El reproductor de audio
        audio = fta.Audio(src="your-audio-file.mp3")
        self.main_page.overlay.append(audio)  # Add to overlay for background play
        self.main_page.add(ft.ElevatedButton("Play", on_click=lambda _: audio.play()))

        self.controls = [
            ft.Text("Mi Playlist", size=30, weight="bold"),
            self.lista_items
        ]