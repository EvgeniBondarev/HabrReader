import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                habrs TEXT
            )
        ''')
        self.conn.commit()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def select_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def new_user(self, user_id, habrs):
        if self.is_user_exists(user_id):
            self.update_user(user_id, habrs)
        else:
            self.add_user(user_id, habrs)

    def add_user(self, user_id, habrs):
        query = f"INSERT INTO users (id, habrs) VALUES ({user_id}, '{habrs}')"
        self.execute_query(query)

    def update_user(self, user_id, habrs):
        query = f"UPDATE users SET habrs = '{habrs}' WHERE id = {user_id}"
        self.execute_query(query)

    def delete_user(self, user_id):
        query = f"DELETE FROM users WHERE id = {user_id}"
        self.execute_query(query)

    def is_user_exists(self, user_id):
        query = f"SELECT * FROM users WHERE id = {user_id}"
        result = self.select_query(query)
        return bool(result)

    def __del__(self):
        self.conn.close()
