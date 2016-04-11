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
            name='Attach',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('file', models.FileField(max_length=128, upload_to='', verbose_name='附件文件')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='最近更新时间')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='所有者')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('detail', models.TextField(blank=True, verbose_name='描述', null=True)),
                ('status', models.CharField(choices=[('0', '无效'), ('1', '有效')], default=1, verbose_name='状态', max_length=2)),
                ('stage', models.CharField(choices=[('1', '收集箱'), ('2', '下一步行动'), ('3', '等待'), ('4', '将来也许'), ('5', '已完成')], default=1, verbose_name='阶段', max_length=2)),
                ('deadline', models.DateTimeField(blank=True, verbose_name='截止时间', null=True)),
                ('estimate', models.TimeField(blank=True, verbose_name='预估时间', null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='最近更新时间')),
                ('agent', models.ForeignKey(verbose_name='代理人', to=settings.AUTH_USER_MODEL, blank=True, related_name='external_task', null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='所有人')),
                ('tag', models.ManyToManyField(blank=True, to='task.Tag', verbose_name='标签', null=True, db_table='task_tag_map')),
                ('upper_task', models.ForeignKey(verbose_name='上一级任务', to='task.Task', blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='attach',
            name='task',
            field=models.ForeignKey(to='task.Task', verbose_name='所属任务'),
        ),
    ]
