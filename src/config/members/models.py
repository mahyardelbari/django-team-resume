import mpmath
from django.db import models

# Create your models here.


class Team(models.Model):
	full_name = models.CharField(max_length=30, verbose_name="full_name", null=True, blank=True)
	avatar = models.ImageField(upload_to="avatar/", null=True, blank=True,)
	role = models.CharField(max_length=30, verbose_name="role", null=True, blank=True)
	linkedin = models.URLField(max_length=200, verbose_name="linkedin", null=True, blank=True)
	github = models.URLField(max_length=200, verbose_name="github", null=True, blank=True)
	telegram = models.URLField(max_length=200, verbose_name="telegram", null=True, blank=True, )
	email = models.EmailField(max_length=220, null=True, blank=True,)
	phone_number = models.IntegerField(null=True, blank=True,)
	resume_document = models.FileField(upload_to='documents/', null=True, blank=True,)
	description = models.TextField(null=True, blank=True)
	shot_description =models.TextField(null=True, blank=True)

	def __str__(self):
		return self.full_name

	class Meta:
		verbose_name = 'عضو تیم'
		verbose_name_plural = 'اعضای تیم'


class UserSkill(models.Model):
	team = models.ForeignKey(Team, related_name='skills', on_delete=models.CASCADE)
	name = models.CharField(max_length=25)
	percent = models.IntegerField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'مهارت'
		verbose_name_plural = 'مهارت ها'
