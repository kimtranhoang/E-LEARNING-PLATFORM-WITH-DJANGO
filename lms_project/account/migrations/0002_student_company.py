# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_remove_company_student'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.Company'),
        ),
    ]
