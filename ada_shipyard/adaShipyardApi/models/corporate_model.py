from django.db import models

class Corporate(models.Model):
    id = models.AutoField(primary_key=True)
    corporate_name = models.CharField(max_length=100)
    corporate_description = models.TextField()
    corporate_image = models.ImageField(upload_to='corporate_images')

    def __str__(self):
        return self.corporate_title