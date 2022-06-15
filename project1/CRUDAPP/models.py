from django.db import models

# Create your models here.
class Laptop(models.Model):
    laptop_id = models.IntegerField()
    name = models.CharField(max_length=70)
    brand = models.CharField(max_length=100)
    ram = models.CharField(max_length=20)
    rom = models.CharField(max_length=20)
    processor = models.CharField(max_length=30)
    price = models.FloatField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.laptop_id}---{self.name}---{self.brand}---{self.price}'