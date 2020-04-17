from django.contrib import admin

# Register your models here.
from .models import Denial, TaskUser

admin.site.register(Denial)
admin.site.register(TaskUser)