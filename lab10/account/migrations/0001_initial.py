# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('user_profile_website', models.URLField(help_text='Ingrese su sitio Web', blank=True, null=True)),
                ('user_profile_picture', models.ImageField(upload_to='profile_images', blank=True, null=True)),
                ('user_profile_identification', models.CharField(help_text='Ingrese su numero de Identificacion', verbose_name='Identificacion', unique=True, max_length=24)),
                ('user_profile', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
