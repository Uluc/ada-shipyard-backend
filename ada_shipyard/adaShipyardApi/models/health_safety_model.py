from django.db import models

class HealthAndSafety(models.Model):
    id = models.AutoField(primary_key=True, default=1)
    health_safety_name = models.CharField(max_length=200)
    health_safety_description = models.TextField()
    health_safety_image = models.ImageField(upload_to='health_safety_images/', blank=True, null=True)