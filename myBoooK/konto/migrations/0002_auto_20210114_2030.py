# Generated by Django 3.1.3 on 2021-01-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='example@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='phoneNumber',
            field=models.IntegerField(default=-111),
        ),
    ]