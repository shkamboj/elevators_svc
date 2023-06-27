from enum import Enum

class DoorState(Enum):
    OPEN = "open"
    CLOSED = "closed"

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]
    

class ElevatorCondition(Enum):
    WORKING = "working"
    NOT_WORKING = "not_working"
    IN_MAINTENANCE = "in_maintenance"

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]
    
class ElevatorDirection(Enum):
    MOVING_UP = "moving_up"
    MOVING_DOWN = "moving_down"
    STILL = "still"
    
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]