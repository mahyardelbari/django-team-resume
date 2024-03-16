from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Project
from .forms import ProjectForm
# Create your views here.


class ProjectFormView(FormView):
	template_name = 'members/formProject.html'
	form_class = ProjectForm
	success_url = "/form-project"

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

