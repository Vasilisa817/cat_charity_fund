from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд поддержки котиков'
    app_description: str = (
        'Наш Фонд собирает пожертвования на различные целевые проекты: '
        'на медицинское обслуживание нуждающихся хвостатых, на обустройство '
        'кошачьей колонии в подвале, на корм оставшимся без попечения '
        'кошкам — на любые цели, связанные с поддержкой кошачьей популяции.')
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'

    secret: str = 'SECRET'
    token_lifetime: int = 3600
    token_url: str = 'auth/jwt/login'
    auth_backend_name = 'jwt'
    password_length = 3
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    str_length = 100

    class Config:
        env_file = '.env'


settings = Settings()
