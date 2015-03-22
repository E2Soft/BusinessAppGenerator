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
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('shortname', models.CharField(null=True, blank=True, max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('shortname', models.CharField(null=True, blank=True, max_length=3)),
                ('cities', models.ManyToManyField(null=True, to='states.City', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('adress', models.CharField(null=True, blank=True, max_length=20)),
                ('phone', models.CharField(null=True, blank=True, max_length=50)),
                ('city', models.ForeignKey(to='states.City')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(to='states.State')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
