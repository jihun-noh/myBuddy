from django.db import models

class ObservationPost(models.Model):
    obs_post_id	= models.CharField(max_length=7, unique=True)
    obs_post_name = models.CharField(max_length=20)
    obs_lat = models.DecimalField(max_digits=999, decimal_places=15)
    obs_lon = models.DecimalField(max_digits=999, decimal_places=15)
    obs_object = models.CharField(max_length=30)
    data_type = models.CharField(max_length=10)

    def __str__(self):
        return self.obs_post_id
