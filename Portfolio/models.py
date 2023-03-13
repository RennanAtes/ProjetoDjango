from django.db import models

# Create your models here.
class MyModel(models.Model):
    upload = models.FileField(upload_to='uploads/')