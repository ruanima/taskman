# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tag',
            field=models.ManyToManyField(verbose_name='标签', blank=True, to='task.Tag', db_table='task_tag_map'),
        ),
    ]
