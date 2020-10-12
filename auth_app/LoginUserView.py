from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login
# from global_constants import constants
# from personnel.constants.user.error_code_constants import PMUserErrorCode
# from handshake_models.user import UserMeta
# from rest.helper.UserHelper import get_user_serialized_data

# META Constants
META_VIEW_CSRF_COOKIE_USED = 'CSRF_COOKIE_USED'
META_VIEW_USER_INFO = 'user_info'
META_VIEW_CSRF_TOKEN = 'csrftoken'
META_VIEW_CSRF_COOKIE_SET = 'csrf_cookie_set'
USERNAME = 'username'
PASSWORD = 'password'
HASH = 'hash'
API_RESP_STATUS_CODE = "status_code"
API_RESP_ERROR_BOOLEAN = "error"
API_RESP_RESULT = "result"
API_RESP_EVENTS = "events"
API_RESP_INVALID_OPERATION = "Invalid_operation"
DATA = 'data'


class LoginUserView(APIView):
    """
    Login api for users
    user needs to provide 'username' and 'password' for authentication.
    """

    validate_keys = [
        USERNAME,
        PASSWORD
    ]

    # authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        try:
            data = dict()
            username = request.data.get(USERNAME, '')
            password = request.data.get(PASSWORD, '')

            # Force updating CSRF cookie
            request.META[META_VIEW_CSRF_COOKIE_USED] = True
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                # Force updating CSRF cookie
                request.META[META_VIEW_CSRF_COOKIE_USED] = True

                print("---1. Login Post method---")
                print("--2. Print Cookie--")
                print(request.COOKIES)
                print("---3. print request--")
                print(request.__dict__)

                if user.is_active:
                    # Login successful and user is active
                    user_info = {HASH: request.session.session_key}
                    data[META_VIEW_USER_INFO] = user_info
                else:
                    data = {API_RESP_ERROR_BOOLEAN: True, API_RESP_RESULT: {
                        API_RESP_INVALID_OPERATION: ["User is inactive"]}}
            else:
                data = {API_RESP_ERROR_BOOLEAN: True, API_RESP_RESULT: {
                    API_RESP_INVALID_OPERATION: ["Invalid username or password"]}}

            request.COOKIES[META_VIEW_CSRF_TOKEN] = get_token(request)

            response = Response(data)
            response[DATA] = data
            response[META_VIEW_CSRF_TOKEN] = get_token(request)
            response[META_VIEW_CSRF_COOKIE_SET] = True
            response.set_cookie(META_VIEW_CSRF_TOKEN, get_token(request))
            return response
        except Exception as e:
            raise e