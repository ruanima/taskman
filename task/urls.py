from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from task import views

urlpatterns = [
    url(r'^$', views.APIRoot.as_view()),
    url(r'^tasks/$', views.TaskList.as_view(), name='task-list'),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(), name='task-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^tags/$', views.TagList.as_view(), name='tag-list'),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view(), name='tag-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
