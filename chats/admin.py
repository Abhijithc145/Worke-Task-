from email import message
from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Organization)
admin.site.register(Department)
admin.site.register(Bot)
admin.site.register(Agent)
admin.site.register(Conversations)
admin.site.register(Message)
admin.site.register(Channel)
admin.site.register(UserProfile)

