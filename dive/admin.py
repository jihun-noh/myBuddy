from django.contrib import admin
from .models import DivePoint, DiveLog, DiveCertOrg

admin.site.register(DivePoint)
admin.site.register(DiveLog)
admin.site.register(DiveCertOrg)
