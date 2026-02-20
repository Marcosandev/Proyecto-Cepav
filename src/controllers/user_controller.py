from src.models.user import User
from src.models.postgres import PostgresConnector

class UserController:
    def __init__(self):
        pass

    def create_user(self, name: str, email: str, password: str = None):
        
        return User.crear_usuario(name, email, password)
        

    def get_users(self):
        return User.obtener_usuarios()
    

    def get_user_by_email(self, email: str):
        """
        Busca un usuario por su dirección de correo electrónico.
        """
        return User.get_one_user(email)

    # --- Interests Management ---
    def save_interests(self, user_id: int, interests: list):
        from src.models.interests import UserInterests
        model = UserInterests()
        model.save_interests(user_id, interests)

    def has_interests(self, user_id: int) -> bool:
        from src.models.interests import UserInterests
        model = UserInterests()
        return model.has_interests(user_id)

    def get_interests(self, user_id: int) -> list:
        from src.models.interests import UserInterests
        model = UserInterests()
        return model.get_interests(user_id)