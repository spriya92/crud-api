from django.conf.urls import url
from auth_app.LoginUserView import LoginUserView

app_name = 'crud'

urlpatterns = [
               url(r'^login/$', LoginUserView.as_view(), name='login'),
               ]