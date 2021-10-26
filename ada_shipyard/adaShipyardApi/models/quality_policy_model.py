from django.db import models

class QualityPolicy(models.Model):
    id = models.AutoField(primary_key=True)

    quality_policy_text = models.CharField(max_length=255)