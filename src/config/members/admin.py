from django.contrib import admin
from .models import UserSkill, Team, ContactUs
# Register your models here.

admin.site.register(Team)
admin.site.register(UserSkill)
admin.site.register(ContactUs)


