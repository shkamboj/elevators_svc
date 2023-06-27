from enum import Enum

class DoorState(Enum):
    OPEN = "open"
    CLOSED = "closed"

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]