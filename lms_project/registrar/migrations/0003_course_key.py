# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0002_auto_20150509_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='key',
            field=models.CharField(max_length=127, default=1),
            preserve_default=False,
        ),
    ]
