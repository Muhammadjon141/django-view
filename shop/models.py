from django.db import models
from vegitables.models import Vegitable, Fruit
from django.contrib.auth.models import User

# Create your models here.
class Shop(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    fruit = models.ManyToManyField(Fruit)
    vegitable = models.ManyToManyField(Vegitable)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    count = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.fruit} {self.vegitable} {self.user} {count}"