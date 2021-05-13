from django.urls import path
from .views import PriciView

urlpatterns = [
    path('pricings/',PriciView.as_view())
]