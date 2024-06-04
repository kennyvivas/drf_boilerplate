from django.contrib import admin
from tasker.model.task import Task
from tasker.model.public_api import PublicApi


class TaskAdmin(admin.ModelAdmin):
    list_display=['created_at','title','user']

admin.site.register(Task,TaskAdmin)

class PublicApiAdmin(admin.ModelAdmin):
    list_display=['title','api_url']

admin.site.register(PublicApi,PublicApiAdmin)