from django.contrib import admin
from . models import HomeModel

# Register your models here.
class HomeModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    
admin.site.register(HomeModel, HomeModelAdmin)