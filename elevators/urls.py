from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElevatorViewSet, ElevatorRequestViewSet

router = DefaultRouter()
router.register(r'elevators', ElevatorViewSet)
router.register(r'elevator-requests', ElevatorRequestViewSet, basename="elevator-requests")

urlpatterns = [
    path('', include(router.urls)),
]