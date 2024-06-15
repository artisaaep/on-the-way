import sqlite3
class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    async def exists(self, user_id) -> bool:
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM Users WHERE id = {user_id}").fetchall()
            return bool(len(result))


    async def create_profile(self, user_id, name="", age=0, sex=-1, photo=-1, bio="", alias="") -> None:
        with self.connection:
            self.cursor.execute(f'INSERT INTO Users (ID, Name, Age, Sex, Photo, Bio, Alias) VALUES ({user_id}, "{name}", {age}, {sex}, "{photo}", "{bio}", "@{alias}")')


    async def update_profile(self, user_id, name=None, age=None, sex=None, photo=None, bio=None) -> None:
        with self.connection:
            if name is not None:
                self.cursor.execute(f'UPDATE Users SET name = "{name}" WHERE id = {user_id}')
            if age is not None:
                self.cursor.execute(f'UPDATE Users SET age = {age} WHERE id = {user_id}')
            if sex is not None:
                self.cursor.execute(f'UPDATE Users SET sex = {sex} WHERE id = {user_id}')
            if photo is not None:
                self.cursor.execute(f'UPDATE Users SET photo = "{photo}" WHERE id = {user_id}')
            if bio is not None:
                self.cursor.execute(f'UPDATE Users SET bio = "{bio}" WHERE id = {user_id}')

    async def get_photo(self, user_id) -> str:
        with self.connection:
            return self.cursor.execute(f"SELECT Photo FROM Users WHERE id = {user_id}").fetchall()[0][0]
