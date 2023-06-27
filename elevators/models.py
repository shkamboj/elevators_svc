from django.db import models

from .choices import DoorState, ElevatorCondition, ElevatorDirection

# Create your models here.



class Elevator(models.Model):
    
    door_state = models.CharField(max_length=32, choices=DoorState.choices(), default=DoorState.CLOSED.value)
    elevator_condtion = models.CharField(max_length=32, choices=ElevatorCondition.choices(), default=ElevatorCondition.WORKING.value)
    current_direction = models.CharField(max_length=32, choices=ElevatorDirection.choices(), default=ElevatorDirection.STILL.value)
    