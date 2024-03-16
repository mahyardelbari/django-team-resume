from django.shortcuts import render
from .models import Slider, SiteSetting
# Create your views here.



def about_us(request):
	setting = SiteSetting.objects.get(is_main_setting=True)
	return render(request, "members/about.html", {'setting': setting})
