from django.db import models

class Hashtag(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'hashtags'

    def __str__(self):
        return self.name
    