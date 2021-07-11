from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=15)
    product_id = models.PositiveIntegerField(unique=True, null=False)

    def __str__(self):
        return self.product_name


class Location(models.Model):
    location = models.CharField(max_length=15)
    location_id = models.PositiveIntegerField(unique=True, null=False)

    def __str__(self):
        return self.location


class ProductMovement(models.Model):
    product_id = models.PositiveIntegerField(unique=True, null=False)
    movement_id = models.PositiveIntegerField(unique=True, null=False)
    timestamp = models.TimeField()
    from_location = models.CharField(max_length=15, blank=True)
    to_location = models.CharField(max_length=15, blank=True)
    location_id = models.PositiveIntegerField(unique=True, null=False)
    qty = models.PositiveIntegerField(null=False)

    def __str__(self):
        return '{} {} '.format(self.location_id, self.qty)
