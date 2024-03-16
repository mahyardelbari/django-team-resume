from django.urls import path
from .views import index, team_member, member_detail


urlpatterns = [
    path('', index, name='index'),
    path('team-member', team_member, name='team-member'),
    path('member-detai/<str:name>', member_detail, name='detail'),
]
