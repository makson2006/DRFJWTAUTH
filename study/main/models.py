from django.db import models

class Men(models.Model):
    full_name = models.CharField(max_length=55)
    age = models.IntegerField()
    description=models.TextField(max_length=5000)

    def __str__(self):
        return self.full_name