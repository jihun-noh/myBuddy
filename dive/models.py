from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class DivePoint(models.Model):
    point_nm = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=999, decimal_places=15)
    longitude = models.DecimalField(max_digits=999, decimal_places=15)
    diver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class DiveLog(models.Model):
    log_nm = models.CharField(max_length=20)
    point_id = models.ForeignKey(DivePoint, on_delete=models.CASCADE)
    dive_date = models.DateTimeField()
    dive_time = models.TimeField()
    temperature = models.SmallIntegerField()
    max_depth = models.SmallIntegerField()
    diver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    buddy = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
