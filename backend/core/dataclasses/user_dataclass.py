from dataclasses import dataclass
from datetime import datetime


@dataclass
class Profile:
    id: int
    name: str
    surname: str
    age: int
    photo: str
    created_at: datetime
    updated_at: datetime


@dataclass
class User:
    id: int
    email: str
    password: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    last_login: datetime
    last_logout: datetime
    created_at: datetime
    updated_at: datetime
    profile: Profile
