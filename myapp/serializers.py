from rest_framework import serializers
from .models import Place, Restaurant, waiter, dish


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = [
            "id",
            "name",
            "location",
        ]


class RestaurantSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(read_only=True)
    place_id = serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(), source="place", write_only=True
    )

    class Meta:
        model = Restaurant
        fields = ["place", "place_id", "name"]


class WaiterSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(), source="restaurant", write_only=True
    )

    class Meta:
        model = waiter
        fields = ["id", "name", "restaurant", "restaurant_id"]


class DishSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(many=True, read_only=True)
    restaurant_ids = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(),
        many=True,
        source="Restaurant",
        write_only=True,
    )

    class Meta:
        model = dish
        fields = ["id", "name", "Restaurant", "restaurant_ids"]
