from django.db import models

class post_id(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()
    summary= models.TextField()
# Create your models here.
