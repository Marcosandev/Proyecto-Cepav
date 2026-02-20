from typing import Optional
from src.models.postgres import PostgresConnector

class User:
    def __init__(self, id: int = None, nickname: str = None, email: str = None, password: str = None):
        self.id = id
        self.nickname = nickname
        self.email = email
        self.password = password

        self.db = PostgresConnector()

    def __repr__(self):
        return f"<User(id={self.id}, nickname='{self.nickname}', email='{self.email}')>"

    @staticmethod
    def get_one_user(email: str) -> Optional['User']:
        """
        Obtiene un usuario específico por su correo electrónico.
        """
        db = PostgresConnector()
        query = "SELECT * FROM users WHERE email=%s;"
        rows = db.execute_query(query, (email,))
        
        # db.execute_query returns a list of dicts based on our implementation
        if rows and len(rows) > 0:
            row = rows[0]
            # Assumes column names match the model attributes or we map them manually
            # Based on previous code: id=row[0], name=row[1], email=row[2], password=row[3]
            # Our executed_query returns dicts: {'id': 1, 'name': 'foo', ...}
            
            print(row)

            
            return User(
                id=row.get('id'),
                nickname=row.get('nickname'), 
                email=row.get('email'), 
                password=row.get('password')
            )
            
        return None
    
    @classmethod
    def crear_usuario(cls, name: str, email: str, password: str):
        
        """
        Crea un nuevo usuario en la base de datos.
        """
        db = PostgresConnector()
        query = """
            INSERT INTO users (nickname, email, password) 
            VALUES (%s, %s, %s) 
            RETURNING id;
        """
        
        user_id = db.execute_query(query, (name, email, password), is_insert=True)
        
        return cls(id=user_id, nickname=name, email=email, password=password)


    @classmethod
    def obtener_usuarios(cls):
        
        """
        Obtiene una lista de todos los usuarios registrados.
        """
        db = PostgresConnector()
        query = "SELECT * FROM users;"
        rows = db.execute_query(query)
        
        users = []
        if rows:
            for row in rows:
                users.append(cls(
                    id=row.get('id'),
                    nickname=row.get('nickname', row.get('name')), # Fallback just in case
                    email=row.get('email'),
                    password=row.get('password')
                ))
        return users

    # We can add a save method here or keep it in the controller as per previous design.
    # The previous design had the controller doing the DB work + using model as data structure.
    # We will stick to that or move login to model. 
    # Let's keep User as a predominantly data class with helper static methods for now.