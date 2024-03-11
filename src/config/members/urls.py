from django.urls import path
from .views import index, team_member, member_detail, form_project, about_us
urlpatterns = [
    path('', index, name='index'),
    path('team-member', team_member, name='team-member'),
    path('member-detai/<str:name>', member_detail, name='detail'),
    path('form-project', form_project, name='form-project'),
    path('about-us', about_us, name='about-us')

]
