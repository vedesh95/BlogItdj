from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_written = models.DateField(auto_now_add=True)
    img_url=models.CharField(max_length=2000)
    title=models.CharField(max_length=50)
    description=models.TextField()
    blog_category=models.CharField(max_length=20,blank=True)
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    subject=models.CharField(max_length=50)
    description=models.TextField()
    contact_number=models.IntegerField()
    def __str__(self):
        return self.username