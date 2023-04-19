from django.contrib import admin
from .models import Task
from .models import Q_logic

admin.site.register(Task)
admin.site.register(Q_logic)

# Register your models here.
