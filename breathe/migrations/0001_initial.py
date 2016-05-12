# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipcode', models.CharField(max_length=5)),
                ('creation_date', models.DateTimeField(editable=False)),
                ('public_flag', models.BooleanField(default=False)),
                ('on_status', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sensor', models.ForeignKey(to='breathe.Sensor')),
                ('subscriber', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
