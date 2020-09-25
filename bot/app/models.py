from django.db import models

class register(models.Model):
    order_name=models.CharField(max_length=100)
    order_mobile=models.IntegerField()
    order_address=models.CharField(max_length=100)
    order_status=models.CharField(max_length=100)