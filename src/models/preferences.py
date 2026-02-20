class UserSettings:
    def __init__(self, id: int = None, dark_mode: bool = False, language: str = "en"):
        self.id = id
        self.dark_mode = dark_mode
        self.language = language

    def __repr__(self):
        return f"<UserSettings(id={self.id}, dark_mode={self.dark_mode}, language='{self.language}')>"