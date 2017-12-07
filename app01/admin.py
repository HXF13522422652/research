from django.contrib import admin

# Register your models here.
from app01 import models
admin.site.register(models.UserInfo)
admin.site.register(models.Grade)
admin.site.register(models.Student)
admin.site.register(models.Questionary)
admin.site.register(models.Quesion)
admin.site.register(models.One_choice)
admin.site.register(models.Answer)

