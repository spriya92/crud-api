from task_2.models import *
from rest_framework import routers, serializers, viewsets


class TaskDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDetails
        fields = ('id','task_type', 'user', 'country', 'start_time', 'end_time')

