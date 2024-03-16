from django.db import models

# Create your models here.


class Project(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    PROJECT_CHOICES = [
	    ('سایت و وبلاگ','سایت و وبلاگ'),
	    ('برنامه های دسکتاپ','برنامه های دسکتاپ'),
	    ('برنامه های موبایل', 'برنامه های موبایل'),
	    ('کارهای مربوط به بخش وب (رسپانسیو سازی و ...)','کارهای مربوط به بخش وب (رسپانسیو سازی و ...)'),
	    ('سایر','سایر'),
    ]
    project_type = models.CharField(max_length=50, choices=PROJECT_CHOICES, default='انتخاب کنید')
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
	    return self.first_name


    class Meta:
	    verbose_name = 'درخواست '
	    verbose_name_plural = 'درخواست ها'
