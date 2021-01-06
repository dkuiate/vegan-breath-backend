from rest_framework import serializers
from .models import Restaurant, Recette,Shop

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class RecetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recette
        fields = '__all__'
