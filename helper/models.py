from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Products(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    session = models.CharField(max_length=100)
    keys = models.BooleanField(default=False)
    battery = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    freeze = models.BooleanField(default=False)
    tire = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(blank=True, null=True, default=0)
    total = models.PositiveIntegerField(blank=True, null=True, default=0)
    language = models.CharField(max_length=20, blank=True, null=True, default='english')

    def __str__(self):
        return self.session

    def get_absolute_url(self):
        return reverse('help:services', kwargs={'user': self.user})