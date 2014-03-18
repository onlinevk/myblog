from django.contrib import admin
from information.models import *
from users.models import *
admin.site.register(User)
admin.site.register(UserType)
admin.site.register(UserLoginAccount)
admin.site.register(Information)
admin.site.register(Comment)

