from django.db import models

# Create your models here.
class Videos(models.Model):
    published_date = models.DateTimeField()
    titles         = models.TextField()
    ids            = models.TextField()
    thumbnails     = models.TextField()
    
    def __str__(self):
        return f'published date : {self.published_date} | title : {self.titles}'