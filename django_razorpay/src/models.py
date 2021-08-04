from django.db import models


class Payment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    number_of_packages = models.IntegerField(default=1)
    instagram = models.CharField(max_length=100,default="Instagram handle")
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
