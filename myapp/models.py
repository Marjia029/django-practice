from django.db import models

# Create your models here.from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)  # Name field
    roll = models.IntegerField(unique=True)  # Roll field (unique for each student)
    mobile = models.CharField(max_length=15)  # Mobile field

    def __str__(self):
        return f"{self.name} ({self.roll})"
