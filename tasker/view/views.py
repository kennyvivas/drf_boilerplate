from rest_framework import viewsets
from tasker.model.task import Task
from tasker.serializers.task_serializer import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer