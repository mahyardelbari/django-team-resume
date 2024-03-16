from django.contrib import admin
from .models import Slider, SiteSetting, TeamResume
# Register your models here.


class SiteSettingAdmin(admin.ModelAdmin):
	list_display = ['is_main_setting']


admin.site.register(SiteSetting, SiteSettingAdmin)
admin.site.register(Slider)
admin.site.register(TeamResume)