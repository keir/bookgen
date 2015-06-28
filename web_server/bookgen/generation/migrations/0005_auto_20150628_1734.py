# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generation', '0004_colorpalette'),
    ]

    operations = [
        migrations.AddField(
            model_name='colorpalette',
            name='med_dark',
            field=models.CharField(default='', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='colorpalette',
            name='med_light',
            field=models.CharField(default='', max_length=6),
            preserve_default=False,
        ),
    ]
