from django.db import models

class Type(models.Model):
    types = models.CharField(max_length=120)
    
    def __str__(self):
        return self.types
    
class Mavsum(models.Model):
    mavsum = models.CharField(max_length=100)
    
    def __str__(self):
        return self.mavsum
    

class Vegitable(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    typee = models.ForeignKey(Type, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='vegitables_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.DecimalField(max_digits=10, decimal_places=2)
    start_sel = models.DateField(auto_now_add=True)
    mavsum = models.ForeignKey(Mavsum, on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ['id']
        
        
    def __str__(self):
        return self.name
    
class Fruit(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    typee = models.ForeignKey(Type, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='fruit_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.DecimalField(max_digits=10, decimal_places=2)
    start_sel = models.DateField(auto_now_add=True)
    mavsum = models.ForeignKey(Mavsum, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.name