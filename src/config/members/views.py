from django.shortcuts import render
from .models import Team, UserSkill
# Create your views here.


def index(request):
	return render(request, 'members/index.html')


def team_member(request):
	member = Team.objects.all()
	return render(request, 'members/team.html', {'member': member})


def member_detail(request, name):
	member = Team.objects.get(full_name=name)
	return render(request, 'members/teamPerson-detalis.html', {'member': member})
