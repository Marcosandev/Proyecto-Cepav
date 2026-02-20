from src.models.preferences import UserSettings
from src.models.postgres import PostgresConnector

class PreferencesController:
    def __init__(self):
        self.db = PostgresConnector()
        self._init_db()

    def _init_db(self):
        """Ensure preferences table exists in Postgres"""
        query = """
        CREATE TABLE IF NOT EXISTS user_settings (
            id SERIAL PRIMARY KEY,
            dark_mode BOOLEAN DEFAULT FALSE,
            language VARCHAR(10) DEFAULT 'en'
        );
        """
        # We don't need a result, just execution. using is_commit=True equivalent logic ideally inside execute_query
        # but execute_query doesn't expose commit flags for DDL easily in my impl?
        # Let's check my PostgresConnector impl. 
        # is_insert adds commit. is_update adds commit. 
        # I can use is_insert=True to force commit or add DDL support. 
        # user's execute_query: "if is_insert: self.connection.commit()"
        # My impl: "if is_insert or is_update: self.connection.commit()"
        # I should probably update PostgresConnector to allow generic commit or just use is_insert=True for now as a hack or update connector.
        # Let's update connector to be more flexible first? No, user wanted "simple".
        # I'll just use execute_query with is_insert=True which commits.
        self.db.execute_query(query, is_insert=True)

    def get_settings(self):
        query = "SELECT * FROM user_settings LIMIT 1;"
        rows = self.db.execute_query(query)
        
        if rows and len(rows) > 0:
            row = rows[0]
            return UserSettings(
                id=row.get('id'), 
                dark_mode=row.get('dark_mode'), 
                language=row.get('language')
            )

        # Create default settings if not exists
        create_query = "INSERT INTO user_settings (dark_mode, language) VALUES (%s, %s) RETURNING id;"
        new_id = self.db.execute_query(create_query, (False, "en"), is_insert=True)
        return UserSettings(id=new_id, dark_mode=False, language="en")

    def update_dark_mode(self, is_dark: bool):
        settings = self.get_settings()
        
        # Postgres syntax %s
        update_query = "UPDATE user_settings SET dark_mode = %s WHERE id = %s;"
        self.db.execute_query(update_query, (is_dark, settings.id), is_update=True)
        
        settings.dark_mode = is_dark
        return settings

