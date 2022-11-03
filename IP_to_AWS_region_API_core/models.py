from django.db import models
from django.contrib.auth.models import User

class IP_to_AWS_region_API(models.Model):
    ip = models.CharField(max_length = 15)

    def __str__(self):
        return self.ip