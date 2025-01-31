import os
from uuid import uuid1


def upload_profile_photo(instance, filename: str) -> str:
    ext = filename.split('.')[-1]
    return os.path.join(instance.user.profile.name, f'{uuid1()}.{ext}')
