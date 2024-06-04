from django.db import models
    
class  PublicApi(models.Model):
    title = models.CharField(max_length=64)
    api_url = models.URLField(max_length=200)

