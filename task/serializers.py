from rest_framework import serializers
from django.contrib.auth.models import User
from task.models import Tag, Task, Attach

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ('id', 'url', 'title', 'owner', 'detail',
                  'status', 'stage', 'deadline', 'upper_task', )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    task_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'task_set')

