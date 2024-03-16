# Generated by Django 4.2.2 on 2024-03-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام')),
                ('family', models.CharField(max_length=300, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(max_length=200, verbose_name='ایمیل')),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField(verbose_name='متن تماس با ما')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('response', models.TextField(null=True, verbose_name='پاسخ تماس با ما')),
                ('is_ready_by_admin', models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس با ما',
            },
        ),
    ]