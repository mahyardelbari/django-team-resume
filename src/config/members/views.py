from django.shortcuts import render
from django.views.generic.edit import FormView
from site_module.models import SiteSetting, Slider, TeamResume
from .models import Team, UserSkill
from .forms import ContactUsForm
# Create your views here.

class ContactUsFormView(FormView):
    template_name = 'members/index.html'
    form_class = ContactUsForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        setting = SiteSetting.objects.get(is_main_setting=True)
        slider = Slider.objects.filter(is_active=True)
        team_resume = TeamResume.objects.filter(is_active=True)
        member = Team.objects.all()
        context['setting'] = setting
        context['slider'] = slider
        context['team_resume'] = team_resume
        context['member'] = member
        return context


def team_member(request):
	member = Team.objects.all()
	return render(request, 'members/team.html', {'member': member})


def member_detail(request, name):
	member = Team.objects.get(full_name=name)
	return render(request, 'members/teamPerson-detalis.html', {'member': member})
# def index(request):
# 	setting = SiteSetting.objects.get(is_main_setting=True)
# 	slider = Slider.objects.filter(is_active=True)
# 	team_resume = TeamResume.objects.filter(is_active=True)
# 	member = Team.objects.all()
#
# 	return render(request, "members/index.html", {'setting': setting,
# 	                                              'slider': slider,
# 	                                              'team_resume': team_resume,
# 	                                              'member': member,
# 	                                              })






