from src.models.postgres import PostgresConnector

class UserInterests:
    def __init__(self):
        self.db = PostgresConnector()
        self._init_db()

    def _init_db(self):
        """Ensure user_interests table exists in Postgres"""
        query = """
        CREATE TABLE IF NOT EXISTS user_interests (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            interest VARCHAR(255) NOT NULL,
            CONSTRAINT fk_user
                FOREIGN KEY(user_id) 
                REFERENCES users(id)
                ON DELETE CASCADE
        );
        """
        # Create index if not exists (optional but good for performance)
        # We'll stick to simple create table for now.
        self.db.execute_query(query, is_insert=True) # Commit handled by is_insert

    def save_interests(self, user_id: int, interests: list[str]):
        """
        Save a list of interests for a user.
        First clears existing interests for the user to avoid duplicates/staleness.
        """
        if not interests:
            return

        # 1. Delete existing interests for this user
        delete_query = "DELETE FROM user_interests WHERE user_id = %s;"
        self.db.execute_query(delete_query, (user_id,), is_update=True)

        # 2. Insert new interests
        insert_query = "INSERT INTO user_interests (user_id, interest) VALUES (%s, %s);"
        for interest in interests:
            self.db.execute_query(insert_query, (user_id, interest), is_insert=True)

    def get_interests(self, user_id: int) -> list[str]:
        """Retrieve all interests for a user."""
        query = "SELECT interest FROM user_interests WHERE user_id = %s;"
        rows = self.db.execute_query(query, (user_id,))
        
        if not rows:
            return []
            
        return [row['interest'] for row in rows]

    def has_interests(self, user_id: int) -> bool:
        """Check if user has any interests saved."""
        query = "SELECT 1 FROM user_interests WHERE user_id = %s LIMIT 1;"
        rows = self.db.execute_query(query, (user_id,))
        return len(rows) > 0
