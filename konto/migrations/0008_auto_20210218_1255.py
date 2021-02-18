# Generated by Django 3.1.3 on 2021-02-18 11:55

from django.conf import settings
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('konto', '0007_auto_20210214_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True, max_length=150, null=True, verbose_name='O mnie'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthDate',
            field=models.DateField(blank=True, null=True, verbose_name='Data urodzin'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='countryOrigin',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Kraj pochodzenia'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='currentLocation',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='Miejscowość'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileAvatar',
            field=models.ImageField(blank=True, default='profilePhoto/default.jpg', upload_to='profilePhoto', verbose_name='Zdjęcie Profilowe'),
        ),
    ]
