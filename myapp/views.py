from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PlaceSerializer, RestaurantSerializer, WaiterSerializer
from rest_framework import status
from .models import Place, Restaurant, waiter


class PlaceView(APIView):

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)


class RestaurantView(APIView):

    def post(self, request):
        place_id = request.data.get("place_id")
        if not place_id:
            return Response(
                {"error": "place_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        if Restaurant.objects.filter(place_id=place_id).exists():
            return Response(
                {"error": "Restaurant for this Place already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, place_id):

        if place_id:
            try:
                restaurant = Restaurant.objects.get(place_id=place_id)
                serializer = RestaurantSerializer(restaurant)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Restaurant.DoesNotExist:
                return Response(
                    {"error": "No restaurant found for this Place ID."},
                    status=status.HTTP_404_NOT_FOUND,
                )


class WaiterView(APIView):
    def post(self, request):
        serializer = WaiterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, restaurant_id):
        restaurant_id = request.query_params.get("restaurant_id")
        if restaurant_id:
            waiters = waiter.objects.filter(restaurant_id=restaurant_id)
            serializer = WaiterSerializer(waiters, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Please provide a restaurant_id in query parameter."},
                status=status.HTTP_400_BAD_REQUEST,
            )
