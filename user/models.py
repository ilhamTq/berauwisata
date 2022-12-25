from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField()
    telp = models.CharField(max_length=14)
    
    def __str__(self):
        return "{} - {}".format(self.user, self.telp)
    
    class Meta:
        verbose_name_plural = "Biodata"
    
    
# class Group(models.Model):
#     nama = models.CharField(max_length=20)
    
#     def __str__(self):
#         return self.nama
    
        
# class User(models.Model):
#     email = models.CharField(max_length=100, blank=True, null=True)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=32)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.username
    