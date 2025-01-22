from django.db import models

# Create your models here.
class HomeModel(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    description = models.CharField()