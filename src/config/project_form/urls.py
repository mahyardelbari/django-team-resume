from django.urls import path
from .views import ProjectFormView

urlpatterns = [
	path('form-project', ProjectFormView.as_view(), name='form-project'),
]