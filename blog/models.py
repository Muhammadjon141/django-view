# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.
# class Blog(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     description = models.TextField()
#     create_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.author}"
    
#     @staticmethod
#     def get_query_set():
#         return Blog.objects.all().order_by('id')