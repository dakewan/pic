from django.contrib import admin
from app01 import models

# Register your models here.
class Imgadmin(admin.ModelAdmin):
    list_display = ("title","summary")
    search_fields = ("title",)
admin.site.register(models.Img,Imgadmin)
