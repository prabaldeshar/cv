from django.contrib import admin

from .models import Job, Project, Skills,Social
# Register your models here.

admin.site.register(Job)
admin.site.register(Project)
admin.site.register(Skills)
admin.site.register(Social)
