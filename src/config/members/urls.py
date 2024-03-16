from django.urls import path
from .views import team_member, member_detail, ContactUsFormView

urlpatterns = [
    path('', ContactUsFormView.as_view(), name='index'),
    path('team-member', team_member, name='team-member'),
    path('member-detai/<str:name>', member_detail, name='detail'),
]