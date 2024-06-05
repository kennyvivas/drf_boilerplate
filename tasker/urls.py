from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tasker.view.views import TaskViewSet,ProcessATaskView


urlpatterns = [
    path('tasks/', TaskViewSet),
    path('tasks/<int:pk>/process/',ProcessATaskView.as_view())  

]

urlpatterns = format_suffix_patterns(urlpatterns)