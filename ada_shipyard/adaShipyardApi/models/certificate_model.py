from django.db import models

class Certificate(models.Model):
    certificate_id = models.AutoField(primary_key=True)
    certificate_name = models.CharField(max_length=255)
    certificate_image = models.ImageField(upload_to='certificates/')
    certificates_description = models.TextField()

