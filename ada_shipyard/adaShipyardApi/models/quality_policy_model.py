from django.db import models

class QualityPolicy(models.Model):
    policy = models.CharField(max_length=255)