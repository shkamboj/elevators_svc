from .models import Elevator
from .choices import ElevatorCondition, DoorState, ElevatorDirection

def process_elevator_request(elevator_request):
    available_elevators = Elevator.objects.filter(elevator_condtion=ElevatorCondition.WORKING.value, 
                                                  door_state=DoorState.CLOSED.value)
    current_floor = elevator_request.current_floor
    distances = [(abs(elevator.current_floor - current_floor), elevator) for elevator in available_elevators]
    distances.sort(key=lambda x: x[0]) # sort the elevators on the basis of distance from current floor
    destination_floor = elevator_request.destination_floor
    closest_elevator = None
    
    
    ### Elevator selection here
    
    # Here, we will pick the elevator, which is either still, OR going in same direction but is just before current floor.
    for distance, elevator in distances:
        if elevator.current_direction == ElevatorDirection.STILL.value or \
        (current_floor < destination_floor and elevator.current_direction == ElevatorDirection.UP.value) or \
        (current_floor > destination_floor and elevator.current_direction == ElevatorDirection.DOWN.value):
            closest_elevator = elevator
            break
    
    # if no criteria is followed from above ones then we will take the first.
    if not closest_elevator:
        closest_elevator = distances[0][1]
        
    if current_floor < destination_floor:
        elevator_new_direction = ElevatorDirection.MOVING_UP.value
    else:
        elevator_new_direction = ElevatorDirection.MOVING_DOWN.value
    
    #### Elevator is moving.. 
    
    closest_elevator.current_direction = elevator_new_direction
    closest_elevator.save()
    
    # -- 
    # --
    # --
    # --
    
    ### Elevator reaches the destination here
    # marking it opened so that, before serving completely, it shouldn't be requested by someone else
    closest_elevator.door_state = DoorState.OPEN.value
    closest_elevator.save()
    
    closest_elevator.current_floor = destination_floor
    closest_elevator.save()
    
    closest_elevator.current_direction = ElevatorDirection.STILL.value
    closest_elevator.save()
    
    # User took an exit from elevator
    
    closest_elevator.door_state = DoorState.CLOSED.value
    closest_elevator.save()
    
    elevator_request.processed = True
    elevator_request.elevator = closest_elevator
    elevator_request.save()
