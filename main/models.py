from datetime import datetime

from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DeviceInformation(models.Model):
    product = models.ForeignKey(Device, on_delete=models.CASCADE)
    total = models.IntegerField(default=0, null=True, blank=True)
    worked = models.IntegerField(default=0, blank=True, null=True)
    broke = models.IntegerField(default=0, blank=True, null=True)
    timestamp = models.DateField(default=datetime.now, blank=True)
    update_at = models.DateField(auto_now=True)
    percentage = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.total and self.worked:
            self.percentage = (self.worked / self.total) * 100
            super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name




