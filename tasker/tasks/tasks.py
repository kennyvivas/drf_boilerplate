import requests
from django.conf import settings
from requests.exceptions import HTTPError
from celery import shared_task
from tasker.services.get_response_from_api import get_response_from_api_service

@shared_task()
def process_task(task_id,url):  
    response = get_response_from_api_service(task_id,url)
    print('Success! ')
    return True
