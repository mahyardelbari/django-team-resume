from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'family', 'email', 'title', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control section-callWe-textbox', 'placeholder': 'نام شما ...'}),
            'family': forms.TextInput(attrs={'class': 'form-control section-callWe-textbox', 'placeholder': 'نام خانوادگی شما...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control section-callWe-textbox', 'placeholder': 'ایمیل...'}),
            'title': forms.TextInput(attrs={'class': 'form-control section-callWe-textbox', 'placeholder': 'موضوع...'}),
            'message': forms.Textarea(attrs={'class': 'form-control section-callWe-textbox section-callWe-textarea', 'placeholder': 'پیام شما...'}),
        }
