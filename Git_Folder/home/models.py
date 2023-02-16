from django.db import models
import os

# Create your models here.

class contact_list(models.Model):
    contact_name = models.CharField(max_length=50, default="None")
    contact_number = models.CharField(max_length=50, default="None")
    email = models.CharField(max_length=50, default="None")
    city = models.CharField(max_length=50, default="None")
    category = models.CharField(max_length=50, default="None")

class add_files(models.Model):
    file_name = models.FileField(upload_to="user_files", null=True)
    
    # def delete(self, *args, **kwargs):
    #     self.user_files.delete()
    #     super().delete(*args, **kwargs)





    




