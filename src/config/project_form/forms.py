from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'title', 'project_type', 'description']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماره تلفن',
            'email': 'ایمیل',
            'title': 'عنوان پروژه',
            'project_type': 'نوع پروژه',
            'description': 'توضیحات'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control section-callWe-textbox', 'placeholder': 'نام شما'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control section-callWe-textbox', 'placeholder': 'نام خانوادگی شما...'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control section-callWe-textbox', 'placeholder': 'شماره تلفن...', 'minlength': '11', 'maxlength': '11'}),
            'email': forms.EmailInput(attrs={'class': 'form-control section-callWe-textbox', 'placeholder': 'ایمیل...'}),
            'title': forms.TextInput(attrs={'class': 'form-control section-callWe-textbox', 'placeholder': 'عنوان پروژه...'}),
            'project_type': forms.Select(attrs={'class': 'form-control select-title-project-form section-callWe-textbox', 'id': 'selectTitleProjectForm'}),
            'description': forms.Textarea(attrs={'class': 'form-control section-callWe-textbox section-callWe-textarea', 'placeholder': 'توضیحاتی درمورد پروژه...'}),
        }
