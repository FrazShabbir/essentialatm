from django.db import models

# Create your models here.
class useracc(models.Model):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50)
    user_email      = models.EmailField(max_length=254)
    user_pass       = models.CharField(max_length=20)
