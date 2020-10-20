from rest_framework import serializers
from .models import Recepee, ShopItem

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepee
        fields = ('title', 'content', 'created_on',  'due_date')

class ShopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopItem
        fields = '__all__'
