from rest_framework import serializers
from django.contrib.auth.models import User
from task.models import Tag, Task, Attach

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'owner', 'detail',
                  'status', 'stage', 'deadline', 'upper_task', )


