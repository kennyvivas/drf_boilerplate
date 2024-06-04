from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tasker.view.views import TaskViewSet


urlpatterns = [
    path('tasks/', TaskViewSet),
]

urlpatterns = format_suffix_patterns(urlpatterns)