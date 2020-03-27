from django.db import models

class board_members(models.Model):
    date_added = models.DateTimeField(auto_now_add=True) 
    date_edited = models.DateTimeField(auto_now=True) 
    member_name = models.CharField(max_length=200, default='')
    position = models.CharField(max_length=200, default='')
    profile = models.TextField(blank=True)
    linkedin = models.CharField(max_length=200, default='')
    profile_pic = models.ImageField(upload_to="img/board", default="img/board/no-image-board.png", null=True, blank=True)
    priority = models.IntegerField()
    
    def __str__(self):
        return self.member_name + ' | ' + self.position + ' | ' + str(self.priority)

class corp_members(models.Model):
    date_added = models.DateTimeField(auto_now_add=True) 
    date_edited = models.DateTimeField(auto_now=True) 
    corp_member_name = models.CharField(max_length=200, default='')
    website = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.corp_member_name

class resources(models.Model):
    date_added = models.DateTimeField(auto_now_add=True) 
    date_edited = models.DateTimeField(auto_now=True) 
    resource_name = models.CharField(max_length=200, default='')
    website = models.CharField(max_length=200, default="", blank=True)
    
    def __str__(self):
        return self.resource_name

class sponsors(models.Model):
    date_added = models.DateTimeField(auto_now_add=True) 
    date_edited = models.DateTimeField(auto_now=True) 
    sponsor_name = models.CharField(max_length=200, default='')
    sponsor_logo = models.ImageField(upload_to="img/sponsors-links", default="img/sponsors-links/no-image-sponsors-links.png", null=True, blank=True)
    website = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.sponsor_name

class pages(models.Model):
    date_added = models.DateTimeField(auto_now_add=True) 
    date_edited = models.DateTimeField(auto_now=True) 
    page_name = models.CharField(max_length=200, default='')
    header = models.CharField(max_length=200, default='')
    content = models.TextField(blank=True)
    url_path = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.page_name + ' | ' + self.url_path