from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .choices import ElevatorCondition, ElevatorDirection, DoorState

from .models import Elevator
from .serializers import ElevatorSerializer

class ElevatorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(url_path = "mark-not-working", detail=True, methods=['PATCH'])
    def mark_not_working(self, request, pk=None):
        elevator = self.get_object()
        elevator.elevator_condition = ElevatorCondition.NOT_WORKING.value
        elevator.save()
        return Response({'message': 'Elevator marked as not working'})

    @action(url_path="mark-in-maintenance", detail=True, methods=['PATCH'])
    def mark_in_maintenance(self, request, pk=None):
        elevator = self.get_object()
        elevator.elevator_condition = ElevatorCondition.IN_MAINTENANCE.value
        elevator.save()
        return Response({'message': 'Elevator marked as in maintenance'})

    @action(url_path="open-door", detail=True, methods=['PATCH'])
    def open_door(self, request, pk=None):
        elevator = self.get_object()
        if elevator.current_direction == ElevatorDirection.STILL.value:
            elevator.door_state = DoorState.OPEN.value
            elevator.save()
            return Response({'message': 'Elevator gate opened'})
        else:
            return Response({'message': 'Gate cannot be opened while elevator is moving'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(url_path="close-door", detail=True, methods=['PATCH'])
    def close_door(self, request, pk=None):
        elevator = self.get_object()
        elevator.door_state = DoorState.CLOSED.value
        elevator.save()
        return Response({'message': 'Elevator door is closed'})