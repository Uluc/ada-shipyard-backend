from django.db import models

class HealthAndSafety(models.Model):
   
    health_safety_title = models.CharField(max_length=200)
    health_safety_description = models.TextField()
    image = models.ImageField(upload_to='health_safety_images/', blank=True, null=True)