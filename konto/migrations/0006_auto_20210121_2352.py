# Generated by Django 3.1.3 on 2021-01-21 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konto', '0005_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phoneNumber',
        ),
        migrations.AddField(
            model_name='profile',
            name='aboutMe',
            field=models.CharField(blank=True, max_length=199),
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='konto.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='users/%Y/%m/%d'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
