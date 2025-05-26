from django.db import models

# Create your models here.
class products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    product_description = models.TextField()
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name