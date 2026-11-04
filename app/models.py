from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    language=models.CharField(max_length=50)
    price=models.IntegerField()
    pages=models.IntegerField()
    image=models.ImageField(upload_to="images",null=True)
    

