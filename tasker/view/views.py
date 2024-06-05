from rest_framework import viewsets,views,permissions,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.utils import json

from tasker.model.task import Task
from tasker.serializers.task_serializer import TaskSerializer
from tasker.tasks.tasks import process_task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ProcessATaskView(views.APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,pk):
        try:
            user = request.user
            _task = Task.objects.get(id=pk,user=user)
            process_task.delay(_task.id)
            return Response({'Success':'Task in on the processing queue','status_code':status.HTTP_200_OK}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error ProcessATaskView':e},status=status.HTTP_400_BAD_REQUEST)