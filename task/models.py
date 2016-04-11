#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

TASK_STATUS = (
    ('0', '无效'),
    ('1', '有效'),
)

TASK_STAGE = (
    ('1', '收集箱'),
    ('2', '下一步行动'),
    ('3', '等待'),
    ('4', '将来也许'),
    ('5', '已完成'),
)


class Tag(models.Model):
    title = models.CharField('标题', max_length=32)
    owner = models.ForeignKey(User, verbose_name='所有者')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified = models.DateTimeField('最近更新时间', auto_now=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField('标题', max_length=128)
    owner = models.ForeignKey(User, verbose_name='所有人')
    agent = models.ForeignKey(User, verbose_name='代理人', null=True, blank=True, related_name='external_task')
    detail = models.TextField('描述', null=True, blank=True)
    tag = models.ManyToManyField(Tag, db_table='task_tag_map', verbose_name='标签', null=True, blank=True)
    status = models.CharField('状态', choices=TASK_STATUS, max_length=2, default=1)
    stage = models.CharField('阶段', choices=TASK_STAGE, max_length=2, default=1)
    deadline = models.DateTimeField('截止时间', null=True, blank=True)
    estimate  = models.TimeField('预估时间', null=True, blank=True)
    upper_task = models.ForeignKey('Task', verbose_name='上一级任务', null=True, blank=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified = models.DateTimeField('最近更新时间', auto_now=True)

    def __str__(self):
        return self.title


class Attach(models.Model):
    task = models.ForeignKey(Task, verbose_name='所属任务')
    file = models.FileField('附件文件', max_length=128)
