# Generated by Django 4.2.2 on 2024-03-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='shot_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]