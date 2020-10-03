from .models import Recepee
from .serializers import TaskSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

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
