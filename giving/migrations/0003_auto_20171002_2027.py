# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giving', '0002_donation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='charity',
            options={'ordering': ['name'], 'get_latest_by': 'founded_date', 'verbose_name_plural': 'charities'},
        ),
    ]
