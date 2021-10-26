from django.db import models

class Section(models.Model):
    corportate_image = models.ImageField(upload_to='corporate_images/', blank=True, null=True)
    facilities_image = models.ImageField(upload_to='facilities_images/', blank=True, null=True)
    projects_image = models.ImageField(upload_to='projects_images/', blank=True, null=True)
    news_image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    contact_image = models.ImageField(upload_to='contact_images/', blank=True, null=True)
    about_image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    home_image = models.ImageField(upload_to='home_images/', blank=True, null=True)