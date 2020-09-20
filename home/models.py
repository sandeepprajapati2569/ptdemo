from django.db import models

# Create your models here.
class url(models.Model):
    url=models.CharField(max_length=500)
