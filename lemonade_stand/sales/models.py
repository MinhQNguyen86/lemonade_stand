from django.db import models
from django.utils import timezone


# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=25)
    position = models.CharField(choices=[('JR', 'Junior'), ('SR', 'Senior'), ('MA', 'Manager')], default='JR',
                                max_length=2)
    commission = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Report(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateTimeField('sale date')
    items = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    commission = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.staff.name + self.date
