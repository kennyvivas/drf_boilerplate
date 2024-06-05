import requests
from django.conf import settings
from requests.exceptions import HTTPError
from celery import shared_task

@shared_task()
def get_response_from_api_service(task_id,url):      
    print(url)
    response = requests.get(url)
    print(response.json())
    return True
