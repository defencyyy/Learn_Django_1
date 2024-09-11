from django.db import models
from datetime import datetime

class User(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  description = models.CharField(blank=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  creation_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.last_name + ", " + self.first_name