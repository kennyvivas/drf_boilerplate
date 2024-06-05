from django.db import models
from django.db.models.signals import post_save
from tasker.model.public_api import PublicApi
from users.models import CustomUser as User
from tasker.tasks.tasks import process_task

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    use_api = models.ForeignKey(PublicApi,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
    

def task_post_save(sender, instance, created, *args, **kwargs):
    if created :
        print(f"task con id {instance.id} se acaba de crear")

        process_task.delay(instance.id,instance.use_api.api_url)
        print(f"Aqui voy a ejecutar una tarea de celery que va a usar el servicio que esta definido en el modelo ")

post_save.connect(task_post_save, sender=Task)