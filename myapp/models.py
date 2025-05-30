from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    join_date = models.DateField()


    def __str__(self):
        return self.name