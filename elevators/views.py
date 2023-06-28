from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .choices import ElevatorCondition, ElevatorDirection, DoorState

from .models import Elevator, ElevatorRequest
from .serializers import ElevatorSerializer, ElevatorRequestSerializer
from .managers import process_elevator_request

class ElevatorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer
    
    # Fetch the next destination floor for a given elevator
    # Fetch if the elevator is moving up or down currently
    ## All these can be looked from GET API -> /api/elevators/1/


    @action(url_path = "mark-not-working", detail=True, methods=['PATCH'])
    def mark_not_working(self, request, pk=None):
        """Mark a elevator as not working
        """
        elevator = self.get_object()
        elevator.elevator_condition = ElevatorCondition.NOT_WORKING.value
        elevator.save()
        return Response({'message': 'Elevator marked as not working'})

    @action(url_path="mark-in-maintenance", detail=True, methods=['PATCH'])
    def mark_in_maintenance(self, request, pk=None):
        """Mark a elevator as in maintenance 
        """
        elevator = self.get_object()
        elevator.elevator_condition = ElevatorCondition.IN_MAINTENANCE.value
        elevator.save()
        return Response({'message': 'Elevator marked as in maintenance'})

    @action(url_path="open-door", detail=True, methods=['PATCH'])
    def open_door(self, request, pk=None):
        """Open the door
        """
        elevator = self.get_object()
        if elevator.current_direction == ElevatorDirection.STILL.value:
            elevator.door_state = DoorState.OPEN.value
            elevator.save()
            return Response({'message': 'Elevator gate opened'})
        else:
            return Response({'message': 'Gate cannot be opened while elevator is moving'}, status=status.HTTP_400_BAD_REQUEST)
    

    @action(url_path="close-door", detail=True, methods=['PATCH'])
    def close_door(self, request, pk=None):
        """Close the door
        """
        elevator = self.get_object()
        elevator.door_state = DoorState.CLOSED.value
        elevator.save()
        return Response({'message': 'Elevator door is closed'})
    
    
    @action(url_path="elevator-requests", detail=True, methods=['GET'])
    def elevator_requests(self, request, pk=None):
        """Fetch all requests for a given elevator
        endpoint : /api/elevators/1/elevator-requests/
        """
        elevator = self.get_object()
        elevator_requests = ElevatorRequest.objects.filter(elevator=elevator)
        result = ElevatorRequestSerializer(elevator_requests, many=True).data
        print(result)
        return Response(result)
    

class ElevatorRequestViewSet(viewsets.ViewSet):
    serializer_class = ElevatorRequestSerializer

    def create(self, request):
        """Saves user request to the list of requests for a elevator
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            elevator_request = serializer.save()
            process_elevator_request(elevator_request)
            data = ElevatorRequestSerializer(elevator_request).data
            print(data)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    