from django.urls import path
from .views import index, team_member, member_detail, about_us, ProjectFormView
urlpatterns = [
    path('', index, name='index'),
    path('team-member', team_member, name='team-member'),
    path('member-detai/<str:name>', member_detail, name='detail'),
    path('form-project', ProjectFormView.as_view(), name='form-project'),
    path('about-us', about_us, name='about-us')

]
