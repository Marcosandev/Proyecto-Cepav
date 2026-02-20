import flet as ft

class ProfileView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("User Profile", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Welcome to your profile page! Here you can view and edit your personal information, check your activity, and manage your settings."),
                ft.Text("This is a placeholder for the user profile content. You can customize it with your own design and functionality."),
            ],
            spacing=20,
            padding=20,
        )