from django.contrib import admin
from auth_app.models import PMUser
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(PMUser)
admin.site.unregister(User)