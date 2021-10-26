from django.db import models

class QualityPolicy(models.Model):
    policy_id = models.AutoField(primary_key=True)

    policy_text = models.CharField(max_length=255)