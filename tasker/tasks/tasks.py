import requests
from django.conf import settings
from requests.exceptions import HTTPError
from celery import shared_task
from tasker.services.get_response_from_api import get_response_from_api_service
from ..model.task import Task

# @shared_task()
# def process_task(task_id,url):  
#     response = get_response_from_api_service(task_id,url)
#     print('Success! ')
#     return True

@shared_task()
def process_task(task_id):
    _task=Task.objects.get(id=task_id)
    _url =  _task.use_api.api_url 
    response = get_response_from_api_service(_task.id,_url)
    _task.status='Completed'
    _task.save()
    print(response)
    print('Success! ')
    return True