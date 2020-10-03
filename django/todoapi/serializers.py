from rest_framework import serializers
from .models import Recepee

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepee
        fields = ('title', 'content', 'created_on',  'due_date')
