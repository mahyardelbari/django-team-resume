from django.shortcuts import render
from django.views.generic.edit import FormView
from site_module.models import SiteSetting, Slider, TeamResume
from .models import Team, UserSkill
# Create your views here.


def index(request):
	setting = SiteSetting.objects.get(is_main_setting=True)
	slider = Slider.objects.filter(is_active=True)
	team_resume = TeamResume.objects.filter(is_active=True)
	print(team_resume)
	return render(request, "members/index.html", {'setting': setting,
	                                              'slider': slider,
	                                              'team_resume': team_resume,
	                                              })



def team_member(request):
	member = Team.objects.all()
	return render(request, 'members/team.html', {'member': member})


def member_detail(request, name):
	member = Team.objects.get(full_name=name)
	return render(request, 'members/teamPerson-detalis.html', {'member': member})





