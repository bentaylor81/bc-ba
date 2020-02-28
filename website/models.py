from django.db import models

class board_members(models.Model):
    member_name = models.CharField(max_length=200, default='')
    position = models.CharField(max_length=200, default='')
    profile = models.TextField(blank=True)
    linkedin = models.CharField(max_length=200, default='')
    image_url = models.CharField(max_length=200, default='')
    priority = models.IntegerField()
    
    def __str__(self):
        return self.member_name + ' | ' + self.position + ' | ' + str(self.priority)

class pages(models.Model):
    page_name = models.CharField(max_length=200, default='')
    header = models.CharField(max_length=200, default='')
    content = models.TextField(blank=True)
    url_path = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.page_name + ' | ' + self.url_path