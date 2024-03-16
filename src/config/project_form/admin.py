from django.contrib import admin
from .models import Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
	list_display = ['first_name', "last_name", 'create_date']
	search_fields = ['project_type']
	list_filter = ['create_date', 'project_type']


admin.site.register(Project, ProjectAdmin)