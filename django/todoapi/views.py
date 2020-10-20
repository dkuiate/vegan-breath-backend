from .models import Recepee, ShopItem
from .serializers import TaskSerializer, ShopItemSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

class RecepeeList(APIView):
    """
    View all Recepees.
    """
    def get(self, request, format=None):
        """
        Return a list of all Recepees.
        """
        tasks = Recepee.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class ShopItemView(viewsets.ModelViewSet):

    serializer_class = ShopItemSerializer
    queryset = ShopItem.objects.all()