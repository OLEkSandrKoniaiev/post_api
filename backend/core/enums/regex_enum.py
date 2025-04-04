from enum import Enum


class RegexEnum(Enum):
    NAME_SURNAME = (
        r'^[A-Za-z]{1,19}$',
        'Only alphabetic letters allowed (1 to 19 characters).',
    )

    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])(\S){8,16}$',
        [
            'password must contain 1 number (0 - 9)',
            'password must contain min 1 uppercase letter',
            'password must contain min 1 lowercase letter',
            'password must contain min 1 alphanumeric character',
            'password min 8 max 16 characters without spaces',
        ],
    )

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
