from django.contrib import admin
from .models import jobModel
from .models import employeeModel

# Register your models here.
admin.site.register(jobModel)
admin.site.register(employeeModel)
