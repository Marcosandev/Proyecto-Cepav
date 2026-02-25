import flet as ft
import os

# Intentamos importar pygame solo si estamos en Windows
# En Android/iOS esta librería no existirá
try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

class PlaylistView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True, spacing=0)
        self.main_page = page
        
        # 1. Configuración del Motor de Audio
        if PYGAME_AVAILABLE:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
        else:
            # Si no hay pygame (Android), usamos el componente nativo de Flet
            self.audio_flet = ft.Audio(src="", autoplay=False)
            self.main_page.overlay.append(self.audio_flet)

        # 2. Componentes de la Interfaz
        self.btn_play_pause = ft.IconButton(
            icon=ft.Icons.PLAY_CIRCLE_FILLED_ROUNDED, 
            icon_size=50, 
            on_click=self._toggle_reproduccion
        )
        
        self.txt_titulo = ft.Text("Selecciona una canción", weight=ft.FontWeight.BOLD, size=16)
        self.txt_artista = ft.Text("Música Local", size=12, color=ft.Colors.GREY_500)
        self.lista_canciones = ft.ListView(expand=True, spacing=10, padding=ft.Padding(20, 20, 20, 20))

        self.controls = [
            self._crear_header(),
            ft.Divider(height=1, color=ft.Colors.GREY_800),
            self.lista_canciones,
            self._crear_barra_controles()
        ]
        
        self._cargar_musica()

    def _crear_header(self):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    width=60, height=60, 
                    bgcolor=ft.Colors.BLUE_GREY_900, 
                    border_radius=10, 
                    content=ft.Icon(ft.Icons.MUSIC_NOTE_ROUNDED, size=30)
                ),
                ft.Column([
                    ft.Text("Mi Biblioteca", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text("Modo: " + ("Windows (Pygame)" if PYGAME_AVAILABLE else "Móvil (Flet Audio)"), 
                            color=ft.Colors.BLUE_400, size=12)
                ])
            ]), 
            padding=ft.Padding(20, 20, 20, 20)
        )

    def _crear_barra_controles(self):
        return ft.Container(
            content=ft.Row([
                ft.Column([self.txt_titulo, self.txt_artista], spacing=0, expand=True),
                self.btn_play_pause,
                ft.Slider(width=100, value=0.8, on_change=self._cambiar_volumen)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            bgcolor=ft.Colors.BLACK, 
            padding=ft.Padding(20, 10, 20, 10)
        )

    def _cambiar_volumen(self, e):
        vol = float(e.data)
        if PYGAME_AVAILABLE:
            pygame.mixer.music.set_volume(vol)
        else:
            self.audio_flet.volume = vol
            self.audio_flet.update()

    def _cargar_musica(self):
        self.lista_canciones.controls.clear()
        rutas_a_buscar = []
        
        # Detectar rutas según el sistema
        user_path = os.path.expanduser("~")
        if os.name == 'nt': # Windows
            rutas_a_buscar = [
                os.path.join(user_path, "Downloads"),
                os.path.join(user_path, "Music")
            ]
        else: # Android / Linux
            rutas_a_buscar = ["/storage/emulated/0/Music", "/sdcard/Download"]

        encontrado = False
        for ruta in rutas_a_buscar:
            if os.path.exists(ruta):
                try:
                    archivos = [f for f in os.listdir(ruta) if f.lower().endswith(".mp3")]
                    for f in archivos:
                        encontrado = True
                        full_path = os.path.join(ruta, f).replace("\\", "/")
                        self.lista_canciones.controls.append(
                            ft.ListTile(
                                title=ft.Text(f, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                                subtitle=ft.Text(f"Carpeta: {os.path.basename(ruta)}", size=10),
                                leading=ft.Icon(ft.Icons.MUSIC_NOTE),
                                on_click=lambda e, p=full_path, t=f: self.reproducir(p, t)
                            )
                        )
                except:
                    continue

        if not encontrado:
            self.lista_canciones.controls.append(ft.Text("No se encontró música", color=ft.Colors.GREY_600))

    def reproducir(self, path, titulo):
        self.txt_titulo.value = titulo
        if PYGAME_AVAILABLE:
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
        else:
            self.audio_flet.src = path
            self.audio_flet.play()
        
        self.btn_play_pause.icon = ft.Icons.PAUSE_CIRCLE_FILLED_ROUNDED
        self.update()

    def _toggle_reproduccion(self, e):
        if self.txt_titulo.value == "Selecciona una canción":
            return
            
        if PYGAME_AVAILABLE:
            if self.btn_play_pause.icon == ft.Icons.PAUSE_CIRCLE_FILLED_ROUNDED:
                pygame.mixer.music.pause()
                self.btn_play_pause.icon = ft.Icons.PLAY_CIRCLE_FILLED_ROUNDED
            else:
                pygame.mixer.music.unpause()
                self.btn_play_pause.icon = ft.Icons.PAUSE_CIRCLE_FILLED_ROUNDED
        else:
            # Lógica para ft.Audio en móvil
            if self.btn_play_pause.icon == ft.Icons.PAUSE_CIRCLE_FILLED_ROUNDED:
                self.audio_flet.pause()
                self.btn_play_pause.icon = ft.Icons.PLAY_CIRCLE_FILLED_ROUNDED
            else:
                self.audio_flet.resume()
                self.btn_play_pause.icon = ft.Icons.PAUSE_CIRCLE_FILLED_ROUNDED
        
        self.update()