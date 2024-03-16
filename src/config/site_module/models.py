from django.db import models

# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200 , verbose_name='نام سایت')
    copy_right = models.CharField(max_length=200 , verbose_name='متن کپی رایت')
    short_about_us = models.TextField(verbose_name='متن بنر')
    about_us_text = models.TextField(verbose_name='درباره ما')
    site_logo = models.ImageField(upload_to='images/site_setting' , verbose_name='لوگوی سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')


    def __str__(self):
        return self.site_name


    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    text = models.CharField(max_length=255, null=True)
    url = models.URLField(verbose_name='لینک', null=True, blank=True)
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک', null=True, blank=True)
    image = models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, null=False)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'


class TeamResume(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    title_url = models.URLField(verbose_name='لینک', null=True, blank=True)
    image = models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'پروژه تیم'
        verbose_name_plural = 'پروژه های تیم'
