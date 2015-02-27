from django.db import models


class Center(models.Model):
    name = models.CharField(blank=True, null=True, max_length=20)
