from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to='projects/', blank=True)
    
    project_length = models.IntegerField()
    project_width = models.IntegerField()
    project_breadth = models.IntegerField()
    project_depth = models.IntegerField()
    project_gross_tonnage = models.IntegerField()

    

    def __str__(self):
        return self.title


    

