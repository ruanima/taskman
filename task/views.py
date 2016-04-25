from task.models import Task, Tag
from task.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from task.serializers import TaskSerializer, UserSerializer, TagSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (permissions.AllowAny,)  # need to del after test

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user.is_authenticated() and self.request.user or None
        # return Task.objects.filter(owner=user)
        return Task.objects.all()

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user.is_authenticated() and self.request.user or None
        # return Task.objects.filter(owner=user)
        return Task.objects.all()


class UserList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)  # need to del after test
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)  # need to del after test
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TagList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)  # need to del after test
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)  # need to del after test
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class APIRoot(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        return Response({
            'users': reverse('user-list', request=request, format=format),
            'tasks': reverse('task-list', request=request, format=format),
            'tags': reverse('tag-list', request=request, format=format),
                        })
