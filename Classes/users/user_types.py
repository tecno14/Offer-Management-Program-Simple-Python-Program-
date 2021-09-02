import enum

class user_types(enum.Enum):
    guest = "guest"
    editor = "editor"
    admin = "admin"
    deny = "deny"