from django.urls import path
from .views import index, team_member, member_detail
urlpatterns = [
    path('', index),
    path('team-member', team_member),
    path('member-detai/<str:name>', member_detail, name='detail')

]
