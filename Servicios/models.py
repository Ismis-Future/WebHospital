from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Services(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/services')
    date = models.DateField()

    def __str__(self):
        pass
