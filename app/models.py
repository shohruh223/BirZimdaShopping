from django.db import models


class Contact(models.Model):
    name = models.CharField()
    phone_number = models.CharField()
    subject = models.CharField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    img = models.ImageField()
    title = models.CharField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField()
    author = models.CharField()

    def __str__(self):
        return self.title



class Product(models.Model):
    img = models.ImageField()
    title = models.CharField()

    review = models.IntegerField(default=0)

    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    old_price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField()

    def __str__(self):
        return self.title