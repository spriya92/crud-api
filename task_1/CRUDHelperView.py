from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response


class MyException(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


# Custom decorator to check the user is authenticated or not
# Also, it checks if the user is active or not
def verify_authentication(function):
    """
    Verify rest is raised by login user.
    :param function:
    :return:
    """
    def is_authentic(self, *args, **kwargs):
        """
        Check user present in request.
        :param self:
        :param args:
        :param kwargs:
        :return:
        """
        user = self.request.user
        user_obj = User.objects.filter(id=user.id)
        if user_obj:
            if not user_obj.is_admin:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return function(self, *args, **kwargs)

    return is_authentic
