import flet as ft

def main(page: ft.Page):
    # Configuración de la página (Blanco y Negro)
    page.title = "Ajustes del Reproductor"
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 600
    page.padding = 20

    # Título
    titulo = ft.Text("AJUSTES", size=30, weight="bold", color="white")

    # Lista de opciones usando nombres en string para evitar errores de atributo
    page.add(
        titulo,
        ft.Divider(color="white24"),
        
        # Opción 1: Tema
        ft.ListTile(
            leading=ft.Icon(name="settings_brightness", color="white"),
            title=ft.Text("Modo Claro", color="white"),
            trailing=ft.Switch(active_color="white"),
        ),
        
        # Opción 2: Volumen
        ft.ListTile(
            leading=ft.Icon(name="volume_up", color="white"),
            title=ft.Text("Volumen Master", color="white"),
            subtitle=ft.Slider(min=0, max=100, value=70, active_color="white"),
        ),
        
        # Opción 3: Info
        ft.ListTile(
            leading=ft.Icon(name="info", color="white"),
            title=ft.Text("Versión de la App", color="white"),
            subtitle=ft.Text("1.0.0 - B&W Style", color="white70"),
        ),

        ft.Container(height=40),
        
        # Botón para cerrar
        ft.ElevatedButton(
            "GUARDAR CAMBIOS",
            style=ft.ButtonStyle(
                color="black",
                bgcolor="white",
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
            width=400,
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)