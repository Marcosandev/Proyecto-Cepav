import flet as ft
from src.views.Theme import *
from src.controllers.User_controller import UserController
from src.views.Homeview import HomeView

class RegisterView( ft.Column ):
    def __init__(self, page):
        super().__init__()
        #--------- Atributos ---------
        self.page = page
        self.controller = UserController()

        self.titulo = ft.Text("Registro", style=FUENTE_TITULO)

        self.nickname_usuario = ft.TextField(
            label="Nickname",
            width=300,
            height=50,
        )

        self.campo_email = ft.TextField(
            label="Email",
            width=300,
            height=50,
        )

        self.campo_contrasena = ft.TextField(
            label="Contraseña",
            width=300,
            height=50,
            password=True,
            can_reveal_password=True,
        )   
        self.boton_registrarse = ft.ElevatedButton(
            text="Registrarse",
            width=200,
            height=50,
            on_click=self.registrarse,
        )
        self.boton_volver = ft.ElevatedButton(
            text="Volver",
            width=200,
            height=50,
            on_click=self.volver,
        )
        self.mensaje = ft.Text("", height=20)

        layout = ft.Column(
            [
                ft.Container(expand=1),
                ft.Row([ft.Image(src="img/em-logo.png", width=250)], alignment=ft.MainAxisAlignment.CENTER),
                
                ft.Column([
                    self.titulo,
                    self.nickname_usuario,
                    self.campo_email,
                    self.campo_contrasena,
                    ft.Column([], height=20),  
                    self.boton_registrarse,
                    self.boton_volver,
                    self.mensaje,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER ),
                ft.Container(expand=1),
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.page.add(layout)
        self.page.update()


    def volver(self, e):
        self.page.clean()
        from src.views.Loginview import LoginView
        self.page.add(LoginView(self.page))
        self.page.update()

    def registrarse(self, e):
        nickname = self.nickname_usuario.value
        email = self.campo_email.value
        password = self.campo_contrasena.value

        if not nickname or not email or not password:
            self.mensaje.value = "Por favor, complete todos los campos."
            self.mensaje.color = ft.Colors.RED
            self.page.update()
            return
        
        try:
            user = self.controller.create_user(nickname, email, password)
            if user:
                print(f"User created: {user}")
                # Para reconocer un usuario registrado
                try:
                    self.page.session.set('user', {'id': user.id, 'nickname': getattr(user, 'nickname', None), 'email': user.email})
                    self.page.session.set('user_id', user.id)
                    self.page.session.set('email', user.email)
                    self.page.session.set('username', getattr(user, 'nickname', None))
                except Exception:
                    pass
                self.mensaje.value = "Registro exitoso!"
                self.mensaje.color = ft.Colors.GREEN
                self.page.update()
                
                # Navigate to HomeView
                self.page.clean()
                self.page.add(HomeView(self.page))
                self.page.update()
        except Exception as ex:
            print(f"Error creating user: {ex}")
            self.mensaje.value = "Error al registrar: el email puede ya existir."
            self.mensaje.color = ft.Colors.RED
            self.page.update()