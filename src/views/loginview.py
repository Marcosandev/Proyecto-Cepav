import flet as ft
from src.views.Theme import *
from src.views.Registerview import RegisterForm
from src.views.Homeview import HomeView
from src.controllers.User_controller import UserController
from src.views.Selectionview import SelectionView

class LoginView(ft.Column):
   """
   Vista de login centralizada y compacta.
   Maneja la autenticación de usuarios y la navegación al registro.
   """

   def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.controller = UserController()

        self.titulo = ft.Text("Event match", style=FUENTE_TITULO)

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

        self.boton_login = ft.ElevatedButton(
            text="Iniciar Sesión",
            width=200,
            height=50,
            on_click=self.login,
        )

        self.boton_registro = ft.ElevatedButton(
            text="Registrarse",
            width=200,
            height=50,
            on_click=self.registrarse,
        )

        self.boton_invitado = ft.TextButton(
            text="Continuar como Invitado",
            width=200,
            height=50,
            on_click=self.invitado,
        )

        self.mensaje = ft.Text("", height=20)

        layout = ft.Column(
            [
                ft.Container(expand=1),
                ft.Row([ft.Image(src="img/em-logo.png", width=250)], alignment=ft.MainAxisAlignment.CENTER),
                ft.Column([ 
                    self.titulo,
                    ft.Column([], height=20),
                    self.campo_email,
                    self.campo_contrasena,
                    ft.Column([], height=10),
                    self.boton_login,
                    ft.Container(height=10),
                    self.boton_registro,
                    self.boton_invitado,
                    self.mensaje
                ], 
                alignment=ft.MainAxisAlignment.CENTER, 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Container(expand=1),
            ],
            expand=True,
        )

        self.page.add(layout)

   def login(self, e):
      """
      Maneja el evento de clic en el botón de iniciar sesión.
      Verifica las credenciales y navega al HomeView si son correctas.
      """
      email = self.campo_email.value
      password = self.campo_contrasena.value

      if not email or not password:
         self.mensaje.value = "Ingrese email y contraseña"
         self.mensaje.color = ft.Colors.RED
         self.page.update()
         return

      user = self.controller.get_user_by_email(email)
      
      if user and user.password == password:
         # Inicio de sesión exitoso
         print(f"Login success: {user.email}")
         
         # Guardar datos en sesión para que HomeView detecte al usuario
         self.page.session.set("user_id", user.id)
         self.page.session.set("email", user.email)
         self.page.session.set("user", {"id": user.id, "email": user.email, "nickname": user.nickname})

         self.page.clean()
         
         # Verificar si el usuario ya tiene intereses guardados
         try:
             if self.controller.has_interests(user.id):
                 self.page.add(HomeView(self.page))
             else:
                 self.page.add(SelectionView(self.page))
         except Exception as ex:
             print(f"Error checking interests: {ex}")
             # Fallback to selection view on error
             self.page.add(SelectionView(self.page))
      else:
         self.mensaje.value = "Credenciales inválidas"
         self.mensaje.color = ft.Colors.RED
         self.page.update()

   def invitado(self, e):
      print("Invitado click ->", e)
      self.page.clean()
      #self.page.add(HomeView(self.page))
      self.page.add(SelectionView(self.page))

   def registrarse(self, e):
      
      self.page.clean()
      RegisterForm(self.page)
      print("Registrarse click ->", e)