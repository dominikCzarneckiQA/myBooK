# Generated by Django 3.1.3 on 2021-01-18 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('img', models.ImageField(upload_to='img/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('creation_date', models.DateField(auto_now_add=True, db_index=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='img_liked', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='img_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]