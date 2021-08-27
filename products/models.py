from django.db import models
# Create your models here.
class Products(models.Model):
    __name = "products"

    name = models.CharField(max_length=100)
    price = models.FloatField()
    qtty = models.IntegerField()
    descr = models.TextField()

    def __str__(self) :
        return self.name 