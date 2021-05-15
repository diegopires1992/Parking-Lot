from django.urls import path
from .views import VehiclesView

urlpatterns = [
    path('vehicles/',VehiclesView.as_view()),
    path('vehicles/<int:vehicle_id>/',VehiclesView.as_view())
]