# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generation', '0003_font'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorPalette',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dark', models.CharField(max_length=6)),
                ('light', models.CharField(max_length=6)),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
    ]
