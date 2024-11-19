from django.db import models

class Keyword(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    class Meta:
        db_table = 'keywords'

    def __str__(self):
        return self.name