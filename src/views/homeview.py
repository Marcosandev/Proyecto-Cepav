import flet as ft
import datetime

class HomeView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__(
            expand=True,
            scroll=ft.ScrollMode.ADAPTIVE,
            spacing=25
        )
        self.main_page = page
        
        # 1. SALUDO DINÁMICO
        self.controls.append(self._crear_cabecera())

        # 2. ACCESO RÁPIDO A BIBLIOTECA
        self.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text("Tu Biblioteca", size=20, weight=ft.FontWeight.BOLD),
                    ft.ResponsiveRow([
                        self._boton_biblioteca("Todas las Canciones", ft.Icons.MUSIC_NOTE_ROUNDED, ft.Colors.BLUE),
                        self._boton_biblioteca("Álbumes", ft.Icons.ALBUM_ROUNDED, ft.Colors.PURPLE),
                        self._boton_biblioteca("Favoritos", ft.Icons.FAVORITE_ROUNDED, ft.Colors.RED),
                    ], spacing=10)
                ]),
                padding=ft.padding.symmetric(horizontal=20)
            )
        )

        # 3. ESCUCHADO RECIENTEMENTE (Cambio aquí)
        self.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text("Escuchado recientemente", size=20, weight=ft.FontWeight.BOLD),
                    self._fila_recientes(),
                ]),
                padding=ft.padding.symmetric(horizontal=20)
            )
        )

    def _crear_cabecera(self):
        hora = datetime.datetime.now().hour
        if 5 <= hora < 12:
            saludo = "¡Buenos días!"
        elif 12 <= hora < 18:
            saludo = "¡Buenas tardes!"
        else:
            saludo = "¡Buenas noches!"

        return ft.Container(
            content=ft.Row([
                ft.Column([
                    ft.Text(saludo, size=28, weight=ft.FontWeight.BOLD),
                    ft.Text("¿Qué vamos a escuchar hoy?", color=ft.Colors.GREY_500),
                ]),
                ft.IconButton(ft.Icons.SETTINGS_ROUNDED, icon_color=ft.Colors.GREY_400)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=ft.padding.only(left=20, right=20, top=20)
        )

    def _boton_biblioteca(self, titulo, icono, color):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icono, color=color, size=30),
                ft.Text(titulo, weight=ft.FontWeight.W_600)
            ], spacing=15),
            bgcolor=ft.Colors.GREY_900 if self.main_page.theme_mode == ft.ThemeMode.DARK else ft.Colors.GREY_100,
            padding=15,
            border_radius=12,
            col={"sm": 12, "md": 4}, 
            on_click=lambda _: print(f"Navegando a: {titulo}"),
        )

    def _fila_recientes(self):
        # Aquí simulamos las últimas canciones que el usuario reprodujo
        recientes = [
            {"name": "Última escuchada", "artist": "Artista Local", "img": ft.Icons.PLAY_CIRCLE_FILL},
            {"name": "Hace 10 min", "artist": "Album Desconocido", "img": ft.Icons.HISTORY},
            {"name": "Ayer", "artist": "Carpeta Música", "img": ft.Icons.AUDIOTRACK},
            {"name": "Favorito antiguo", "artist": "Desconocido", "img": ft.Icons.MUSIC_NOTE},
        ]

        items = []
        for s in recientes:
            items.append(
                ft.Container(
                    content=ft.Column([
                        ft.Container(
                            # Usamos una caja gris oscuro para simular la portada
                            content=ft.Icon(s["img"], size=50, color=ft.Colors.BLUE_GREY_400),
                            width=150, height=150,
                            bgcolor=ft.Colors.GREY_900 if self.main_page.theme_mode == ft.ThemeMode.DARK else ft.Colors.GREY_300,
                            border_radius=15,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Text(s["name"], weight=ft.FontWeight.BOLD, size=14, max_lines=1),
                        ft.Text(s["artist"], size=12, color=ft.Colors.GREY_400, max_lines=1)
                    ]),
                    width=150,
                    on_click=lambda e, name=s["name"]: print(f"Reproduciendo desde recientes: {name}")
                )
            )
        return ft.Row(items, scroll=ft.ScrollMode.ADAPTIVE, spacing=20)