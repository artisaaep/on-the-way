import sqlite3


class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    async def exists(self, user_id) -> bool:
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM Users WHERE id = {user_id}").fetchall()
            self.connection.commit()
            return bool(len(result))

    async def create_profile(self, user_id, name="", age=0, sex=-1, alias="") -> None:
        with self.connection:
            self.cursor.execute(
                f'INSERT INTO Users (ID, Name, Age, Sex, Alias) VALUES ({user_id}, "{name}", {age}, {sex}, "@{alias}")')
            self.connection.commit()

    async def update_profile(self, user_id, name=None, age=None, sex=None) -> None:
        with self.connection:
            if name is not None:
                self.cursor.execute(f'UPDATE Users SET name = "{name}" WHERE id = {user_id}')
            if age is not None:
                self.cursor.execute(f'UPDATE Users SET age = {age} WHERE id = {user_id}')
            if sex is not None:
                self.cursor.execute(f'UPDATE Users SET sex = {sex} WHERE id = {user_id}')
            self.connection.commit()