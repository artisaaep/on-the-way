async def exists(user_id) -> bool:
    """Возвращает true если юзер с таким айди уже есть в бд"""
    return False


async def create_profile(user_id, name=None, age=None, sex=None, photo=None, bio=None) -> None:
    """Создает профиль"""


async def update_profile(user_id, name=None, age=None, sex=None, photo=None, bio=None) -> None:
    """Обновляет данные в существующем профиле"""

