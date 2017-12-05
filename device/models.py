from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class DeviceManager(models.Manager):
    def get_object_or_none(self, number):
        try:
            device = super(DeviceManager, self).get_queryset().get(number=number)
        except:
            device = None
        return device


class Device(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    number = models.CharField(max_length=10, unique=True)
    network_operator = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DeviceManager()

    def __str__(self):
        return "%s - %s" % (self.user.username, self.number)


class Tracking(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=255, default=0)
    longitude = models.CharField(max_length=255, default=0)
    capture_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.device
