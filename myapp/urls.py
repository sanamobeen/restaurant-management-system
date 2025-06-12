from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PlaceView, RestaurantView, WaiterView

urlpatterns = [
    path("myapp/create_place/", PlaceView.as_view(), name="place"),
    path(
        "myapp/get_restaurant/<int:place_id>/", RestaurantView.as_view(), name="place"
    ),
    path("myapp/WaiterView/", WaiterView.as_view(), name="Waiter"),
]
