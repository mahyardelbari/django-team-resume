from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Team, UserSkill
from .forms import ProjectForm
# Create your views here.


def index(request):
	return render(request, 'members/index.html')


def team_member(request):
	member = Team.objects.all()
	return render(request, 'members/team.html', {'member': member})


def member_detail(request, name):
	member = Team.objects.get(full_name=name)
	return render(request, 'members/teamPerson-detalis.html', {'member': member})

def about_us(request):
	return render(request, 'members/about.html')

class ProjectFormView(FormView):
	template_name = 'members/formProject.html'
	form_class = ProjectForm
	success_url = "/form-project"

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)





# def form_project(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_url')  # مسیر موفقیت آمیز
#     else:
#         form = ProjectForm()
#     return render(request, 'members/formProject.html', {'form': form})


