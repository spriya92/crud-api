from task_2.serializers import TaskDetailsSerializer
from rest_framework.views import APIView
from task_2.models import TaskDetails
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import datetime

# Create your views here.


class TaskDetail(APIView):
    """

    """
    @staticmethod
    def post(request):
        """

        :param request:
        :return:
        """
        try:
            # Pass request data to task detail serializer
            serializer = TaskDetailsSerializer(data=request.data)
            # Check validation of serializer
            if serializer.is_valid():
                serializer.save()
                if serializer.data['end_time'] < datetime.datetime.now():
                    return True
                else:
                    return False

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TaskDetails.DoesNotExist:
            raise Http404
