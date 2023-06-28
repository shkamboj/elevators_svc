from rest_framework import serializers
from .models import Elevator, ElevatorRequest

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = '__all__'
        

# class ElevatorRequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ElevatorRequest
#         fields = ['current_floor', 'destination_floor']
#         read_only_fields = ['elevator']



class ElevatorRequestSerializer(serializers.ModelSerializer):
    elevator = serializers.PrimaryKeyRelatedField(read_only=True)
    processed = serializers.BooleanField(read_only=True)

    class Meta:
        model = ElevatorRequest
        fields = '__all__'
