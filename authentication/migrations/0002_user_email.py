# Generated by Django 4.2.1 on 2023-09-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, null=True, unique=True),
        ),
    ]
