from django.db import models

class contact(models.Model):
    date_added = models.DateTimeField(auto_now_add=True) 
    name = models.CharField(max_length=200, default='')
    company = models.CharField(max_length=200, default='')
    position = models.CharField(max_length=200, default='')
    address = models.TextField(blank=True)
    zip_code = models.CharField(max_length=200, default='')
    phone = models.IntegerField()
    email = models.CharField(max_length=200, default='')
    website = models.CharField(max_length=200, default='')
    comments = models.TextField(blank=True)
    
    def __str__(self):
        return self.name