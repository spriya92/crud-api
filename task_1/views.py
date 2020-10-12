from task_1.serializers import MovieDetailsSerializer
from rest_framework.views import APIView
from task_1.models import MovieDetails
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from task_1.CRUDHelperView import verify_authentication, MyException
from django.contrib.auth.models import User

# Create your views here.


class GetList(APIView):
    """
    Get and Post call to create and get movie
    """
    def get(self, request, format=None ):
        """

        :param request:
        :param format:
        :return:
        """
        try:
            user_obj = User.objects.filter(id=self.request.user.id)
            if user_obj:
                # Get search text param
                search_txt = self.request.GET.get('search_txt', '')
                # Filter search text of movies
                users = MovieDetails.objects.filter(
                    name__icontains=search_txt
                )
                # Pass data to serializer to validate
                serializer = MovieDetailsSerializer(users, many=True)

                return Response(serializer.data)
            else:
                raise MyException('User obj not present')

        except MyException as x:
            raise x

    @staticmethod
    @verify_authentication
    def post(request):
        """

        :param request:
        :return:
        """
        try:
            # Pass request data to movie detail serializer
            serializer = MovieDetailsSerializer(data=request.data)
            # Check validation of serializer
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MovieDetails.DoesNotExist:
            raise Http404


class MovieDetail(APIView):
    """
    Update or Delete a movie instance.
    """
    @staticmethod
    def get_object(pk):
        """

        :param pk:
        :return:
        """
        try:
            # Get movie detail object
            return MovieDetails.objects.get(pk=pk)
        except MovieDetails.DoesNotExist:
            raise Http404

    @verify_authentication
    def put(self, request, pk):
        """

        :param request:
        :param pk:
        :return:
        """
        try:
            user = self.get_object(pk)
            serializer = MovieDetailsSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MovieDetails.DoesNotExist:
            raise Http404

    @verify_authentication
    def delete(self, pk):
        """

        :param pk:
        :return:
        """
        try:
            user = self.get_object(pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MovieDetails.DoesNotExist:
            raise Http404
