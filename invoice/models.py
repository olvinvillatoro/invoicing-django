from django.db import models

# Create your models here.
class Invoice(models.Model):
    __name = "invoice"

    name = models.CharField(max_length=100)
    date = models.DateField()
