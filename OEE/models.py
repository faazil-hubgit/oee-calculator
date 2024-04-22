from django.db import models


# Create your models here.
# datatable for machines

class machines(models.Model):
    machine_name = models.CharField(max_length=100)
    machine_serial_no = models.CharField(max_length=100)
    time = models.TimeField(null=True)


import uuid


class product_log(models.Model):
    cycle_no = models.IntegerField()
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material_name = models.CharField(max_length=100)
    machine= models.CharField(max_length=100)

    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    duration = models.IntegerField()
    good_products = models.IntegerField()
    bad_product = models.IntegerField()


class oee(models.Model):
    machine_name=models.CharField(max_length=100)
    machine_OEE = models.CharField(max_length=100)