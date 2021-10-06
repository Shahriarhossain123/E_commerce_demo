from django.db import models


# Create your models here.
class Products(models.Model):
    title = models.CharField("Title", max_length=200)
    price = models.FloatField("Price")
    discount_price = models.FloatField("Discount Price")
    category = models.TextField("Category")
    description = models.TextField("Description")
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title