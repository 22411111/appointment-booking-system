from django.db import models

# Create your models here.
class Appointment(models.Model):
    Name = models.CharField(max_length=200)
    service = models.CharField(max_length=200)
    number_of_people = models.IntegerField()
    Date = models.DateField()
    email = models.TextField()

    def __str__(self):
        return self.Name
    
