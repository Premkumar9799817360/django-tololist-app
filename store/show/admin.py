from django.contrib import admin
from .models import Storage
# Register your models here.
admin.site.register(Storage)
class Storage(admin.ModelAdmin):
    list_display =['id','name','mobile','email']
