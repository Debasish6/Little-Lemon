from django.db import models
from datetime import datetime

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=200)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.name
 
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField() 
    
    def __str__(self):
        return f'{self.Title} : {self.Price}'   
