from django.db import models

# Create your models here.
class Batch(models.Model):
    batch = models.CharField(max_length=50)
    academic_year = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    intake = models.CharField(max_length=50)

    def __str__(self):
        return self.batch