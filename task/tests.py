from django.test import TestCase
from django.contrib.auth.models import User
from .models import *


class TagTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username='test_user', password='123')
        Tag.objects.create(title='a test tag', owner=user1, )

    def tearDown(self):
        pass

    def test_tag(self):
        tag1 = Tag.objects.get(title='a test tag')
        self.assertEqual(tag1.owner.username, 'test_user')


class TaskTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username='test_user', password='123')
        tag1 = Tag.objects.create(title='a test tag', owner=user1, )
        task1 = Task.objects.create(title='A test task',
                                    owner=user1,
                                    detail='this my first task.',)
        task1.tag.add(tag1)

    def test_task(self):
        task1 = Task.objects.get(title='A test task')
        self.assertEqual(task1.owner.username, 'test_user')
        self.assertEqual(task1.tag.all()[0].title, 'a test tag')
        self.assertEqual(task1.get_stage_display(), '收集箱')
        self.assertEqual(task1.get_status_display(), '有效')
