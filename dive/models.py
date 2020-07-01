from django.db import models
from django.conf import settings
from account.models import User

class DivePoint(models.Model):
    point_id = models.CharField(max_length=20, primary_key=True)
    point_nm = models.CharField(max_length=20, unique=True)
    latitude = models.DecimalField(max_digits=999, decimal_places=15)
    longitude = models.DecimalField(max_digits=999, decimal_places=15)
    diver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.point_id

class DiveLog(models.Model):
    log_id = models.CharField(max_length=20, primary_key=True)
    log_nm = models.CharField(max_length=20, unique=True)
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
        return self.log_id
