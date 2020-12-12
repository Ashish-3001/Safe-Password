from django.db import models

# Create your models here.
class Application(models.Model):

    name = models.CharField(max_length=100)
    

class Password(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    key = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    
