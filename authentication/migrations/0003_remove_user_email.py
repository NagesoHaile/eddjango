# Generated by Django 4.2.1 on 2023-09-11 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]