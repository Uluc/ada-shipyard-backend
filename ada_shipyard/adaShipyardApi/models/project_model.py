from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    length = models.IntegerField()
    width = models.IntegerField()
    breadth = models.IntegerField()
    depth = models.IntegerField()
    gross_tonnage = models.IntegerField()

    image = models.ImageField(upload_to='projects/', blank=True)

    def __str__(self):
        return self.title


    

