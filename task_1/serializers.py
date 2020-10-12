from task_1.models import *
from rest_framework import routers, serializers, viewsets


class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDetails
        fields = ('id','name')

