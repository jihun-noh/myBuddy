from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class DivePoint(models.Model):
    point_nm = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=999, decimal_places=10)
    longitude = models.DecimalField(max_digits=999, decimal_places=10)
    diver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class DiveLog(models.Model):
    log_nm = models.CharField(max_length=20)
    point_id = models.ForeignKey(DivePoint, on_delete=models.CASCADE)
    dive_date = models.DateTimeField()
    dive_time = models.TimeField(blank=True)
    temperature = models.SmallIntegerField(blank=True, null=True)
    max_depth = models.SmallIntegerField(blank=True, null=True)
    diver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    buddy = models.EmailField(blank=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class DiveCertOrg(models.Model):
    org_name = models.CharField(max_length=20)
    cert_level = models.CharField(max_length=20)
    cert_step = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str('{}_{}'.format(self.org_name, self.cert_level))
