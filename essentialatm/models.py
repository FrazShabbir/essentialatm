from django.db import models

# Create your models here.
class useracc(models.Model):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50)
    email           = models.EmailField(max_length=254)
    user_pass       = models.CharField(max_length=20)
    balance         = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username
