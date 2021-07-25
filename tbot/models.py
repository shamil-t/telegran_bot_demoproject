from django.db import models

# Create your models here.

class User_Model(models.Model):
  user_id  = models.CharField(max_length=100)
  user_name = models.CharField(max_length=100)
  
  fat_count = models.IntegerField(default=0)
  stupid_count = models.IntegerField(default=0)
  dump_count = models.IntegerField(default=0)

  def __str__(self):
      return "{} - {}".format(self.user_id, self.user_name)