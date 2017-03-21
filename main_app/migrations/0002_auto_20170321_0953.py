# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='img_url',
            field=models.ImageField(default='media/default.png', upload_to='treasure_images'),
        ),
    ]
