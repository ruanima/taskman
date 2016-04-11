# -*- coding:utf-8 -*-

# from django.conf import settings
# from django.db import models

# USER_GENDERS = (
#     ('0', u'未指定'),
#     ('m', u'男'),
#     ('f', u'女')
# )

# class TUser(models.models):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL)
#     avatar = models.ImageField('图片', null=True, blank=True)
#     mobile = models.CharField('手机号码', max_length=64, blank=True, null=True, db_index=True)
#     gender = models.CharField('性别', choices=USER_GENDERS, default='0', max_length=1)

#     class Meta:
#         db_table = 'account_user'
#         verbose_name = '用户'
#         verbose_name_plural = '用户'