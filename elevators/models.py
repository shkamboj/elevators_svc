from django.db import models

from .choices import DoorState

# Create your models here.



class Elevator(models.Model):
    
    door_state = models.CharField(max_length=20, choices=DoorState.choices(), default=DoorState.CLOSED.value)
