from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='default value')

class Test(models.Model):
    thing = models.TextField(default='testsad;lfjas;ljk')
