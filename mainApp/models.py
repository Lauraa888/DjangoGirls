from django.db import models

class post(models.Model):
    
    title = models.CharField(max_length=120)
    post = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.title

