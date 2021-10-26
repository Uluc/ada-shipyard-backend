from django.db import models

class News(models.Model):
    id = models.AutoField(primary_key=True)
    news_name = models.CharField(max_length=200)
    news_description = models.TextField()
    news_image = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return self.title


    