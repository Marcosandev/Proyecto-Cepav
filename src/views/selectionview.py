import flet as ft

class SelectionView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.ADAPTIVE
        )
        self.page = page
        
        self.seleccionados = []
        
        opciones = [
            "Conferencias Congresos", "Ferias Comerciales",
            "Eventos Sociales", "Seminarios Talleres",
            "Lanzamientos de Producto", "Eventos Deportivos",
            "Conciertos Espectáculos", "Eventos de Networking",
            "Eventos Benéficos", "Eventos Culturales"
        ]

        self.controls.append(
            ft.Container(
                content=ft.TextField(prefix_icon=ft.Icons.SEARCH, border_radius=20, height=45),
                padding=20
            )
        )

        self.grid = ft.ResponsiveRow(spacing=10, run_spacing=10)
        for opcion in opciones:
            self.grid.controls.append(
                ft.Container(
                    content=ft.Text(opcion, text_align=ft.TextAlign.CENTER, size=12, color="black"),
                    bgcolor="white",
                    border=ft.border.all(1, "black"),
                    border_radius=5,
                    padding=10,
                    col={"xs": 6}, 
                    on_click=self.toggle_selection,
                    data=opcion 
                )
            )
        
        self.controls.append(self.grid)

        
        self.btn_confirmar = ft.ElevatedButton(
            "Confirmar",
            disabled=True,
            on_click=self.ir_a_siguiente,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
            width=250,
            height=50
        )
        
        self.controls.append(ft.Container(self.btn_confirmar, padding=30))

    def toggle_selection(self, e):
        opcion = e.control.data
        
        if opcion in self.seleccionados:
            
            self.seleccionados.remove(opcion)
            e.control.bgcolor = "white"
        elif len(self.seleccionados) < 3:
          
            self.seleccionados.append(opcion)
            e.control.bgcolor = ft.Colors.BLUE_100 
        self.btn_confirmar.disabled = len(self.seleccionados) != 3
        self.update()

    def ir_a_siguiente(self, e):
        self.page.session.set("mis_eventos", self.seleccionados)
        
        # Guardar en base de datos si hay usuario
        user_id = self.page.session.get("user_id")
        if user_id:
            from src.controllers.User_controller import UserController
            controller = UserController()
            # Run in a safe block or async if needed, but for now direct call
            try:
                controller.save_interests(user_id, self.seleccionados)
            except Exception as ex:
                print(f"Error saving interests: {ex}")

        from src.views.Homeview import HomeView
        
        self.page.clean()
        self.page.add(HomeView(self.page))
        # self.page.update()