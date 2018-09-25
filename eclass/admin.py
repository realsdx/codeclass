from django.contrib import admin
from eclass import models

# Register your models here.
admin.site.register(models.Assignment)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Problem)
admin.site.register(models.CodeClass)